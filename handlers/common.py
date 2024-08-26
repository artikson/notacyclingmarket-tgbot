from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.keyboards import main_kb

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "<b>Главное меню</b>",
        reply_markup=main_kb()
    )

@router.callback_query(F.data == "cancel_ad_creating")
@router.callback_query(F.data == "move_to_main_menu")
async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer(
        "<b>Главное меню</b>",
        reply_markup=main_kb()
    )
    await callback.answer()
