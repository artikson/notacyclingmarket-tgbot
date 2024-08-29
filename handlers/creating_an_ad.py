from aiogram import Router, F, types, Bot
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.creating_an_ad_keyboard import start_creating_an_ad, end_creating_ad

from middlewares.album_middleware import AlbumMiddleware

router = Router()
router.message.middleware(AlbumMiddleware())

class AddAnAd(StatesGroup):
    sending_ad_photos = State()
    sending_ad_description = State()
    sending_ad = State()

@router.callback_query(StateFilter(None), F.data == "add_an_advert")
async def start_an_ad_creating(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "<b>(1/?) Создание объявления</b>\nОтправьте фотографии вашего товара:",
        reply_markup=start_creating_an_ad()
    )
    await state.set_state(AddAnAd.sending_ad_photos)
    await callback.answer()

@router.message(
    AddAnAd.sending_ad_photos,
    F.media_group_id
)
async def album_sended(
    message: Message,
    state: FSMContext,
    album: list[Message]
):
    media_group = []
    for msg in album:
        file_id = msg.photo[-1].file_id
        media_group.append(file_id)
    await message.answer(
        "<b>(2/?) Создание объявления</b>\nСпасибо. Теперь отправьте описание вашего товара:",
        reply_markup=start_creating_an_ad()
    )
    await state.update_data(sended_photos=media_group)
    await state.set_state(AddAnAd.sending_ad_description)

@router.message(
    AddAnAd.sending_ad_photos,
    F.photo
)
async def photo_sended(
    message: Message,
    state: FSMContext
):
    await state.update_data(sended_photos=message.photo[-1].file_id)
    await message.answer(
        "<b>(2/?) Создание объявления</b>\nСпасибо. Теперь отправьте описание вашего товара:",
        reply_markup=start_creating_an_ad()
    )
    await state.set_state(AddAnAd.sending_ad_description)

@router.message(AddAnAd.sending_ad_photos)
async def photo_sended_incorrectly(message: Message):
    await message.answer(
        "<b>Ошибка</b>\nПожалуйста, отправьте фотографии вашего товара.",
        reply_markup=start_creating_an_ad()
    )

@router.message(
    AddAnAd.sending_ad_description,
    F.text
)
async def description_sended(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.update_data(description_text=message.text)
    await state.update_data(description_user_first_name=message.from_user.first_name)
    await state.update_data(description_user_id=message.from_user.username)
    if type(user_data['sended_photos']) == str:
        await message.answer_photo(
            photo = user_data['sended_photos'],
            caption = message.text
        )
    else:
        album_builder = MediaGroupBuilder(
            caption=message.text
        )
        for photo in user_data['sended_photos']:
            album_builder.add_photo(
                media=photo
            )
        await message.answer_media_group(
            album_builder.build(),
            reply_markup=None
        )
    await message.answer(
        "<b>Публикация</b>\nВаше объявление выглядит так",
        reply_markup=end_creating_ad()
    )
    await state.update_data(sended_description=message.text)
    await state.set_state(AddAnAd.sending_ad)

@router.message(AddAnAd.sending_ad_description)
async def description_sended_incorrectly(message: Message):
    await message.answer(
        "<b>Ошибка</b>\nПожалуйста, отправьте описание вашего товара\.",
    )

@router.callback_query(
    AddAnAd.sending_ad, 
    F.data == "send_ad",
)
async def ad_sending(callback: types.CallbackQuery, bot: Bot, state: FSMContext):
    user_data = await state.get_data()
    if type(user_data['sended_photos']) == str:
        await bot.send_photo(
            "@notacyclingmarket", 
            photo=user_data['sended_photos'], 
            caption=(
                f"Описание товара:\n{user_data['sended_description']}\n\n\n\n"
                f"Информация о пользователе:\n{user_data['description_user_first_name']}\n"
                f"@{user_data['description_user_id']}"
            )
        )
    else:
        album_builder = MediaGroupBuilder(
            caption=(
                f"Описание товара:\n{user_data['sended_description']}\n\n\n\n"
                f"Информация о пользователе:\n{user_data['description_user_first_name']}\n"
                f"@{user_data['description_user_id']}"
            )
        )
        for photo in user_data['sended_photos']:
            album_builder.add_photo(
                media=photo
            )
        await bot.send_media_group("@notacyclingmarket", media=album_builder.build())
    await callback.answer()
    await state.clear()