from aiogram import types
from aiogram.types import InlineKeyboardMarkup

def start_creating_an_ad() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Домой", callback_data="move_to_main_menu")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def bulletin_board_kb() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Добавить объявление", callback_data="add_an_advert")],
        [types.InlineKeyboardButton(text="Домой", callback_data="move_to_main_menu")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def end_creating_ad() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Отправить", callback_data="send_ad")],
        [types.InlineKeyboardButton(text="Домой", callback_data="move_to_main_menu")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard