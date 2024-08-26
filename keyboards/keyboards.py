from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def main_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="🏆 Доска объявлений",
        callback_data="bulletin_board")
    )
    return kb.as_markup()

def bulletin_board_kb() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Добавить объявление", callback_data="add_an_advert")],
        [types.InlineKeyboardButton(text="Домой", callback_data = "move_to_main_menu")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def move_to_main_menu_board_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Домой",
        callback_data="move_to_main_menu")
    )
    return kb.as_markup()