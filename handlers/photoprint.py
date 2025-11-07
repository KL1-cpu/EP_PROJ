from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.photoprint import get_photo_format_keyboard, get_photo_print_type_keyboard
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

@router.message(F.text == "📸 ФОТОПЕЧАТЬ")
async def photoprint_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.photo_format)
    await state.update_data(service_type="Фотопечать", previous_menu='main')
    
    info_text = (
        "📸 ФОТОПЕЧАТЬ\n\n"
        "ℹ️ Печать производится только на глянцевой бумаге\n\n"
        "Выберите формат бумаги:"
    )
    
    await message.answer(info_text, reply_markup=get_photo_format_keyboard())

@router.message(OrderStates.photo_format)
async def photo_format_selected(message: Message, state: FSMContext):
    await state.update_data(format=message.text)
    await state.set_state(OrderStates.photo_print_type)
    await message.answer(
        "Выберите тип печати фото:",
        reply_markup=get_photo_print_type_keyboard()
    )

@router.message(OrderStates.photo_print_type)
async def photo_print_type_selected(message: Message, state: FSMContext):
    await state.update_data(print_type=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )