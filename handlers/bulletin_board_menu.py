# from aiogram import Router, F, types
# from aiogram.filters import Command
# from aiogram.types import Message, ReplyKeyboardRemove

# from keyboards.keyboards import main_kb

# router = Router()

# @router.message(Command("start"))
# async def cmd_start(message: Message):
#     await message.answer(
#         "Выберите пункт меню",
#         reply_markup=main_kb()
#     )

# @router.callback_query(F.data == "to_add_an_advert")
# async def answer_bulletin_board(callback: types.CallbackQuery):
#     await callback.message.answer(
#         "Создание объявления"
#     )
#     await callback.answer()