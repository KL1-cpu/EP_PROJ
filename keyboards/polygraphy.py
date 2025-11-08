from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Главное меню полиграфии
def get_polygraphy_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ВИЗИТКИ"), KeyboardButton(text="БЛОКНОТЫ")],
            [KeyboardButton(text="БУКЛЕТЫ"), KeyboardButton(text="КАЛЕНДАРИ")],
            [KeyboardButton(text="КОНВЕРТЫ"), KeyboardButton(text="ЛИСТОВКИ")],
            [KeyboardButton(text="ПЕЧАТЬ НА САМОКЛЕЙКЕ"), KeyboardButton(text="ПЛАКАТЫ")],
            [KeyboardButton(text="СЕРТИФИКАТЫ"), KeyboardButton(text="СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Визитки
def get_business_card_print_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Офсетная"), KeyboardButton(text="Цифровая")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_business_card_offset_color_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="4+0 (односторонние)"), KeyboardButton(text="4+4 (двусторонние)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_business_card_offset_quantity_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1000 шт."), KeyboardButton(text="2500 шт.")],
            [KeyboardButton(text="5000 шт."), KeyboardButton(text="10000 шт.")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_business_card_digital_paper_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Картон 310 г/м²"), KeyboardButton(text="Лен")],
            [KeyboardButton(text="Маджестик"), KeyboardButton(text="Фактурная")],
            [KeyboardButton(text="Плайк")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_business_card_digital_lamination_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без ламинации"), KeyboardButton(text="Глянцевая"), KeyboardButton(text="Матовая")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_business_card_digital_quantity_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="50 шт."), KeyboardButton(text="100 шт."), KeyboardButton(text="200 шт.")],
            [KeyboardButton(text="300 шт."), KeyboardButton(text="1000 шт.")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Блокноты
def get_notebook_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A6"), KeyboardButton(text="A5"), KeyboardButton(text="A4")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_notebook_inner_block_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Офсетная 80 г/м² без печати")],
            [KeyboardButton(text="Офсетная 80 г/м² с цветной печатью")],
            [KeyboardButton(text="Офсетная 80 г/м² с Ч/Б печатью")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_notebook_cover_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Мелованная бумага 250 г/м² с печатью")],
            [KeyboardButton(text="Мелованная бумага 300 г/м² с печатью")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_notebook_backing_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="С печатью"), KeyboardButton(text="Без печати")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_notebook_stitching_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="По короткому краю"), KeyboardButton(text="По длинному краю")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_notebook_pages_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="20 стр."), KeyboardButton(text="40 стр.")],
            [KeyboardButton(text="60 стр."), KeyboardButton(text="80 стр.")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Буклеты
def get_booklet_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A4 (в сложенном виде)"), KeyboardButton(text="A5 (в сложенном виде)")],
            [KeyboardButton(text="A6 (в сложенном виде)"), KeyboardButton(text="Евроформат (в сложенном виде)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_booklet_paper_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Мелованная 115 г/м²"), KeyboardButton(text="Мелованная 130 г/м²")],
            [KeyboardButton(text="Мелованная 150 г/м²"), KeyboardButton(text="Мелованная 250 г/м²")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_booklet_color_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="4+0 (односторонняя)"), KeyboardButton(text="4+4 (двухсторонняя)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_booklet_fold_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Один сгиб"), KeyboardButton(text="Два сгиба"), KeyboardButton(text="Гармошка")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Календари
def get_calendar_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Квартальный"), KeyboardButton(text="Домик")],
            [KeyboardButton(text="Карманный (кратно 8 шт.)"), KeyboardButton(text="Перекидной А4")],
            [KeyboardButton(text="Перекидной А3")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Конверты
def get_envelope_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Евроконверт"), KeyboardButton(text="Формат C5")],
            [KeyboardButton(text="Формат C6"), KeyboardButton(text="Конверт для CD")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Листовки
def get_leaflet_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A4 (210×297 мм)"), KeyboardButton(text="A5 (148×210 мм)")],
            [KeyboardButton(text="A6 (105×148 мм)"), KeyboardButton(text="A7 (74×105 мм)")],
            [KeyboardButton(text="Евроформат (210×99 мм)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_leaflet_paper_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Мелованная 115 г/м²"), KeyboardButton(text="Мелованная 130 г/м²")],
            [KeyboardButton(text="Мелованная 150 г/м²"), KeyboardButton(text="Офсетная 80 г/м²")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Печать на самоклейке
def get_sticker_material_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пленка белая мат."), KeyboardButton(text="Пленка белая гл.")],
            [KeyboardButton(text="Пленка прозрач. мат."), KeyboardButton(text="Пленка прозрач. гл.")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_sticker_print_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A4 (210×297 мм)"), KeyboardButton(text="A3 (297×420 мм)"), KeyboardButton(text="SRA3 (320×450 мм)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_sticker_cutting_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Да"), KeyboardButton(text="Нет")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Плакаты
def get_poster_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A3 (297×420 мм) - цифровая печать")],
            [KeyboardButton(text="A2 (420×594 мм) - интерьерная печать")],
            [KeyboardButton(text="A1 (594×841 мм) - интерьерная печать")],
            [KeyboardButton(text="A0 (841×1189 мм) - интерьерная печать")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_poster_paper_type_a3_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Офсетная 80 г/м²"), KeyboardButton(text="Мелованная 115 г/м²")],
            [KeyboardButton(text="Мелованная 130 г/м²"), KeyboardButton(text="Мелованная 150 г/м²")],
            [KeyboardButton(text="Мелованная 170 г/м²"), KeyboardButton(text="Мелованная 250 г/м²")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_poster_cutting_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Подрезка нужна"), KeyboardButton(text="Подрезка не нужна")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_poster_paper_type_large_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Постерная бумага 150 г/м²"), KeyboardButton(text="Постерная бумага 200 г/м²")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Сертификаты
def get_certificate_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A4 (210×297 мм)"), KeyboardButton(text="A5 (148×210 мм)")],
            [KeyboardButton(text="A6 (105×148 мм)"), KeyboardButton(text="Евроформат (210×99 мм)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )


def get_certificate_paper_type_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Мелованная 150 г/м²"), KeyboardButton(text="Мелованная 170 г/м²"), KeyboardButton(text="Мелованная 250 г/м²")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_certificate_lamination_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Без ламинации"), KeyboardButton(text="Глянцевая"), KeyboardButton(text="Матовая")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

# Стикеры с плоттерной резкой
def get_sticker_pack_material_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пленка белая мат."), KeyboardButton(text="Пленка белая гл.")],
            [KeyboardButton(text="Пленка прозрач. мат."), KeyboardButton(text="Пленка прозрач. гл.")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_sticker_pack_format_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="A4 (210×297 мм)"), KeyboardButton(text="A3 (297×420 мм)")],
            [KeyboardButton(text="A5 стикерпак (148×210 мм)"), KeyboardButton(text="A6 стикерпак (105×148 мм)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_sticker_pack_color_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="4+0 (односторонняя)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )

def get_sticker_pack_cut_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Да (включена в стоимость)")],
            [KeyboardButton(text="Нет (только печать)")],
            [KeyboardButton(text="🏠 Главное меню")]
        ],
        resize_keyboard=True
    )