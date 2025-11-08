from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.stamps import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

@router.message(F.text == "🏢 ИЗГОТОВЛЕНИЕ ПЕЧАТЕЙ И ШТАМПОВ")
async def stamps_main(message: Message, state: FSMContext):
    await state.set_state(OrderStates.stamp_type)
    await state.update_data(service_type="Изготовление печатей и штампов", previous_menu='main')
    
    info_text = (
        "🖋️ ИЗГОТОВЛЕНИЕ ПЕЧАТЕЙ И ШТАМПОВ\n\n"
        "ℹ️ При заказе печати ООО необходимо предоставить:\n"
        "• Учредительные документы ООО\n"
        "• Доверенность на получение печати\n\n"
        "ℹ️ Индивидуальный предприниматель получает печать с паспортом\n\n"
        "ℹ️ При заказе печати врача необходимо предоставить диплом врача\n\n"
        "Выберите тип печати:"
    )
    
    await message.answer(info_text, reply_markup=get_stamp_type_keyboard())

@router.message(OrderStates.stamp_type)
async def stamp_type_selected(message: Message, state: FSMContext):
    await state.update_data(stamp_type=message.text)
    await state.set_state(OrderStates.stamp_format)
    await message.answer(
        "Выберите формат печати:",
        reply_markup=get_stamp_format_keyboard()
    )

@router.message(OrderStates.stamp_format)
async def stamp_format_selected(message: Message, state: FSMContext):
    await state.update_data(format=message.text)
    await state.set_state(OrderStates.stamp_ink_color)
    await message.answer(
        "Выберите цвет штемпельной подушки:",
        reply_markup=get_stamp_ink_color_keyboard()
    )

@router.message(OrderStates.stamp_ink_color)
async def stamp_ink_color_selected(message: Message, state: FSMContext):
    await state.update_data(ink_color=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]], 
            resize_keyboard=True
        )
    )