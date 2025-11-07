from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню интерьерной печати
def get_interior_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ПЛАКАТЫ"), KeyboardButton(text="ТАБЛИЧКИ")],
            [KeyboardButton(text="КАРТИНЫ НА ХОЛСТЕ"), KeyboardButton(text="ПЕЧАТЬ НА БАННЕРЕ")],
            [KeyboardButton(text="ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Таблички
def get_sign_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Офисные таблички"), KeyboardButton(text="Уличные таблички")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_sign_material_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пластик ПВХ-3 мм"), KeyboardButton(text="Пластик ПВХ-5 мм")],
            [KeyboardButton(text="Двухслойный пластик")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Картины на холсте
def get_canvas_size_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="20×30 см"), KeyboardButton(text="30×40 см")],
            [KeyboardButton(text="40×50 см"), KeyboardButton(text="40×60 см")],
            [KeyboardButton(text="50×50 см"), KeyboardButton(text="50×70 см")],
            [KeyboardButton(text="60×80 см"), KeyboardButton(text="70×100 см")],
            [KeyboardButton(text="80×120 см")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_canvas_framing_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без подрамника"), KeyboardButton(text="Галерейная натяжка")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Печать на баннере
def get_banner_print_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Широкоформатная"), KeyboardButton(text="Интерьерная")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_banner_edge_processing_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без обработки"), KeyboardButton(text="Укрепление края")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_banner_grommets_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без люверсов"), KeyboardButton(text="Люверсы через 30 см")],
            [KeyboardButton(text="Люверсы через 50 см")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Печать на самоклейке
def get_interior_sticker_film_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Матовая самоклеющаяся плёнка"), KeyboardButton(text="Глянцевая самоклеющаяся плёнка")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_interior_sticker_processing_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без обработки"), KeyboardButton(text="Ламинация")],
            [KeyboardButton(text="Подрезка напечатанного макета"), KeyboardButton(text="Плоттерная резка")],
            [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )