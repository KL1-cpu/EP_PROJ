from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_stamps_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="АВТОМАТИЧЕСКАЯ ПЕЧАТЬ"), KeyboardButton(text="КАРМАННАЯ ПЕЧАТЬ")],
            [KeyboardButton(text="ФАКСИМИЛЕ"), KeyboardButton(text="КЛИШЕ БЕЗ ОСНАСТКИ")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_stamp_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Автоматическая печать"), KeyboardButton(text="Карманная печать")],
            [KeyboardButton(text="Факсимиле"), KeyboardButton(text="Клише без оснастки")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_stamp_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Круглая 30 мм"), KeyboardButton(text="Круглая 40 мм")],
            [KeyboardButton(text="Прямоугольный штамп")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_stamp_ink_color_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Черный"), KeyboardButton(text="Фиолетовый")],
            [KeyboardButton(text="Красный"), KeyboardButton(text="Зелёный")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )