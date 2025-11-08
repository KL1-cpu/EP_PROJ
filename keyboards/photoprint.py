from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_photo_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="10×15"), KeyboardButton(text="15×21"), KeyboardButton(text="21×30")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_photo_print_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="С полями (изображение полностью, возможны белые поля)")],
            [KeyboardButton(text="Без полей (изображение займёт всю площадь, возможна обрезка краёв)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )