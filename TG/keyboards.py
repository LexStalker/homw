from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоимость"),
            KeyboardButton(text="О нас")

        ]
    ],resize_keyboard=True
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя игра", callback_data="medium")],
        [InlineKeyboardButton(text="Большая игра", callback_data="large")],
        [InlineKeyboardButton(text="Мега игра", callback_data="extra large")],
        [InlineKeyboardButton(text="Другие предложения", callback_data="other")]
    ]
)
buy_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить", url="http://google.ru")],
        [InlineKeyboardButton(text="Назад", callback_data="back_to_catalog")]
    ]
)