from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Ч/Б печать
def get_bw_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A4"), KeyboardButton(text="A3")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bw_print_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Односторонняя"), KeyboardButton(text="Двусторонняя")],
            [KeyboardButton(text="Печать брошюры")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bw_additional_services_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Брошюровка на металлическую пружину")],
            [KeyboardButton(text="Пластиковые обложки")],
            [KeyboardButton(text="Скрепление брошюры")],
            [KeyboardButton(text="Пропустить")]
        ],
        resize_keyboard=True
    )

# Цветная печать
def get_color_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A7 (74×105 мм)"), KeyboardButton(text="A6 (105×148 мм)")],
            [KeyboardButton(text="Евроформат (210×99 мм)"), KeyboardButton(text="A5 (148×210 мм)")],
            [KeyboardButton(text="A4 (210×297 мм)"), KeyboardButton(text="A3 (297×420 мм)")]
        ],
        resize_keyboard=True
    )

def get_color_paper_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Офсетная 80 г/м²")],
            [KeyboardButton(text="Мелованная 115 г/м²"), KeyboardButton(text="Мелованная 130 г/м²")],
            [KeyboardButton(text="Мелованная 170 г/м²"), KeyboardButton(text="Мелованная 250 г/м²")],
            [KeyboardButton(text="Мелованная 300 г/м²")],
            [KeyboardButton(text="Пленка белая мат."), KeyboardButton(text="Пленка белая гл.")],
            [KeyboardButton(text="Пленка прозрач. мат."), KeyboardButton(text="Пленка прозрач. гл.")],
        ],
        resize_keyboard=True
    )

def get_color_additional_services_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Брошюровка на металлическую пружину")],
            [KeyboardButton(text="Пластиковые обложки")],
            [KeyboardButton(text="Скрепление брошюры")],
            [KeyboardButton(text="Подрезка")],
            [KeyboardButton(text="Пропустить")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Общие клавиатуры для копицентра
def get_copycenter_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Ч/Б ПЕЧАТЬ"), KeyboardButton(text="ЦВЕТНАЯ ПЕЧАТЬ")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_files_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            # [KeyboardButton(text="📎 Прикрепить файлы")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_comment_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📝 Добавить примечание")],
            [KeyboardButton(text="Пропустить")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_order_confirmation_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Отправить заказ-подтверждение")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )