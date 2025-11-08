from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню упаковки
def get_packaging_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ПАКЕТЫ"), KeyboardButton(text="КОРОБКИ")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Пакеты - выбор типа
def get_bag_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Бумажные пакеты"), KeyboardButton(text="ПВД пакеты")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Бумажные пакеты
def get_bag_paper_print_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Печать с одной стороны пакета")],
            [KeyboardButton(text="Печать с 2 сторон с одного макета")],
            [KeyboardButton(text="Печать с 2 сторон разные макеты")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bag_paper_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="220×330×70 мм"), KeyboardButton(text="195×320×90 мм")],
            [KeyboardButton(text="100×330×100 мм"), KeyboardButton(text="170×220×70 мм")],
            [KeyboardButton(text="70×330×70 мм"), KeyboardButton(text="130×220×70 мм")],
            [KeyboardButton(text="120×140×70 мм"), KeyboardButton(text="210×210×100 мм")],
            [KeyboardButton(text="210×210×80 мм"), KeyboardButton(text="330×220×70 мм")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bag_paper_lamination_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Матовое"), KeyboardButton(text="Глянцевое")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bag_paper_grommets_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Золото"), KeyboardButton(text="Серебро")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bag_paper_handle_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Белые"), KeyboardButton(text="Чёрные")],
            [KeyboardButton(text="Красные"), KeyboardButton(text="Синие")],
            [KeyboardButton(text="Зелёные"), KeyboardButton(text="Жёлтые")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# ПВД пакеты
def get_bag_pvd_print_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1+0"), KeyboardButton(text="1+1")],
            [KeyboardButton(text="2+0"), KeyboardButton(text="2+2")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_bag_pvd_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="20×30 см"), KeyboardButton(text="30×40 см")],
            [KeyboardButton(text="40×50 см"), KeyboardButton(text="50×60 см")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Коробки - выбор материала
def get_box_material_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Коробки из мелованного картона"), KeyboardButton(text="Коробки из микро-гофры")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Коробки из мелованного картона
def get_box_cardboard_print_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без печати"), KeyboardButton(text="Полноцветная печать")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Коробки из микро-гофры
def get_box_corrugated_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="95×55×90 мм"), KeyboardButton(text="115×95×65 мм")],
            [KeyboardButton(text="180×55×55 мм"), KeyboardButton(text="360×150×50 мм")],
            [KeyboardButton(text="415×160×60 мм"), KeyboardButton(text="200×200×10 мм")],
            [KeyboardButton(text="Индивидуальный размер")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_box_corrugated_color_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Белый"), KeyboardButton(text="Коричневый")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_box_corrugated_logo_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без нанесения"), KeyboardButton(text="С нанесением")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )