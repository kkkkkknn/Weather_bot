from aiogram import types
from aiogram.types import ReplyKeyboardMarkup

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Погода'), types.KeyboardButton(text='Статистика')],
        [types.KeyboardButton(text='Рестарт'), types.KeyboardButton(text='Справка')],

    ],
    resize_keyboard=True
)
