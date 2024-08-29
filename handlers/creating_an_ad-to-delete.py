# from aiogram import Router, F, types
# from aiogram.filters import StateFilter
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.types import Message

# from keyboards.creating_an_ad_keyboard import creating_an_ad_1, creating_an_ad_2

# router = Router()

# class AddAnAd(StatesGroup):
#     sending_ad_photos = State()
#     sending_ad_description = State()

# @router.callback_query(StateFilter(None), F.data == "add_an_advert")
# async def answer_to_add_an_advert(callback: types.CallbackQuery, state: FSMContext):
#     await callback.message.answer(
#         "Отправьте фотографию вашего товара:",
#         reply_markup=creating_an_ad_1()
#     )
#     await state.set_state(AddAnAd.sending_ad_photos)
#     await callback.answer()

# @router.message(
#     AddAnAd.sending_ad_photos,
#     F.photo
# )
# async def photos_sended(message: Message, state: FSMContext):
#     await state.update_data(sended_photos=message.photo)
#     await message.answer(
#         text="Спасибо. Теперь отправьте описание вашего товара:",
#         reply_markup=creating_an_ad_2()
#     )
#     await state.set_state(AddAnAd.sending_ad_description)