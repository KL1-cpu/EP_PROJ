from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню сувениров
def get_souvenirs_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="РУЧКИ С ЛОГОТИПОМ"), KeyboardButton(text="ФУТБОЛКИ")],
            [KeyboardButton(text="КРУЖКИ")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Ручки
def get_pen_material_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пластик"), KeyboardButton(text="Металл"), KeyboardButton(text="Крафт (картон)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_pen_color_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Синий"), KeyboardButton(text="Красный"), KeyboardButton(text="Черный")],
            [KeyboardButton(text="Белый"), KeyboardButton(text="Серебристый"), KeyboardButton(text="Золотистый")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# def get_pen_application_keyboard():
#     return ReplyKeyboardMarkup(
#         keyboard=[
#             [KeyboardButton(text="Лазерная гравировка"), KeyboardButton(text="УФ-печать")],
#             [KeyboardButton(text="🏠 Главное меню")]
#         ],
#         resize_keyboard=True
#     )

# Футболки
def get_tshirt_size_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="XS"), KeyboardButton(text="S"), KeyboardButton(text="M")],
            [KeyboardButton(text="L"), KeyboardButton(text="XL"), KeyboardButton(text="XXL")],
            [KeyboardButton(text="XXXL")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_tshirt_material_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Хлопок 100% (белый)")],
            [KeyboardButton(text="Хлопок 100% (черный)")],
            [KeyboardButton(text="Хлопок 50% / Полиэстер 50% (белый)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_tshirt_print_position_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="На груди"), KeyboardButton(text="На спине")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Кружки
def get_mug_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Кружка белая"), KeyboardButton(text="Кружка цветная внутри, цветная ручка")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_mug_print_position_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="С одной стороны"), KeyboardButton(text="По кругу"), KeyboardButton(text="С двух сторон")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_mug_packaging_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без упаковки"), KeyboardButton(text="Подарочная коробка")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )