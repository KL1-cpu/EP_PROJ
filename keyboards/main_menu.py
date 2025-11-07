from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_main_menu_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📄 КОПИЦЕНТР", callback_data="copycenter")],
        [InlineKeyboardButton(text="🖨️ ПОЛИГРАФИЯ", callback_data="polygraphy")],
        [InlineKeyboardButton(text="📦 УПАКОВКА", callback_data="packaging")],
        [InlineKeyboardButton(text="🖼️ ИНТЕРЬЕРНАЯ ПЕЧАТЬ", callback_data="interior")],
        [InlineKeyboardButton(text="🎁 СУВЕНИРЫ", callback_data="souvenirs")],
        [InlineKeyboardButton(text="🏢 ИЗГОТОВЛЕНИЕ ПЕЧАТЕЙ И ШТАМПОВ", callback_data="stamps")],
        [InlineKeyboardButton(text="📸 ФОТОПЕЧАТЬ", callback_data="photoprint")]
    ])