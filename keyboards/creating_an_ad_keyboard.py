from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def creating_an_ad_1() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Домой", callback_data="move_to_main_menu")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def creating_an_ad_2() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Домой", callback_data="move_to_main_menu")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def end_creating_ad() -> InlineKeyboardMarkup:
    buttons = [
        [types.InlineKeyboardButton(text="Отменить", callback_data="cancel_ad_creating")],
        [types.InlineKeyboardButton(text="Отправить", callback_data="send_ad")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard