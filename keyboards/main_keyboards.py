from aiogram import types
from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def main_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="🏆 Доска объявлений",
        callback_data="bulletin_board")
    )
    return kb.as_markup()

def move_to_main_menu_board_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(types.InlineKeyboardButton(
        text="Домой",
        callback_data="move_to_main_menu")
    )
    return kb.as_markup()