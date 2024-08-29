from aiogram import Router, types, F

from keyboards.creating_an_ad_keyboard import bulletin_board_kb

router = Router()

@router.callback_query(F.data == "bulletin_board")
async def answer_bulletin_board(callback: types.CallbackQuery):
    await callback.message.answer(
        "<b>Доска объявлений</b>",
        reply_markup=bulletin_board_kb()
    )
    await callback.answer()