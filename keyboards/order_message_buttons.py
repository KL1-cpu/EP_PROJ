from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_confirm_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="❌ Подтвердить", callback_data="confirm")]
    ])
    return keyboard

def get_confirmed_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Подтверждено", callback_data="confirmed")]
    ])
    return keyboard