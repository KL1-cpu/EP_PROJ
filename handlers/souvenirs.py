from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.souvenirs import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Главное меню сувениров
@router.message(F.text == "🎁 СУВЕНИРЫ")
async def souvenirs_main(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await message.answer(
        "Раздел СУВЕНИРЫ. Выберите продукт:",
        reply_markup=get_souvenirs_main_keyboard()
    )

# РУЧКИ С ЛОГОТИПОМ
@router.message(F.text == "РУЧКИ С ЛОГОТИПОМ")
async def pens_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.pen_material)
    await state.update_data(Услуга="Ручки с логотипом", previous_menu='souvenirs')
    await message.answer(
        "✏️ РУЧКИ С ЛОГОТИПОМ\n\nВыберите материал корпуса:",
        reply_markup=get_pen_material_keyboard()
    )

@router.message(F.text == "Пластик")
async def pen_material_selected_2(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.pen_color)
    await message.answer(
        "Выберите цвет корпуса:",
        reply_markup=get_pen_color_keyboard()
    )

@router.message(F.text == "Крафт (картон)")
async def pen_material_selected_3(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.pen_color)
    await message.answer(
        "Выберите цвет корпуса:",
        reply_markup=get_pen_color_keyboard()
    )

@router.message(F.text == "Металл")
async def pen_application_selected(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.pen_application)
    await message.answer(
        "Выберите способ нанесения:",
        reply_markup=get_pen_application_keyboard()
    )

@router.message(OrderStates.pen_application)
async def pen_color_selected(message: Message, state: FSMContext):
    await state.update_data(Нанесение=message.text)
    await state.set_state(OrderStates.pen_color)
    await message.answer(
        "Выберите цвет корпуса:",
        reply_markup=get_pen_color_keyboard()
    )

@router.message(OrderStates.pen_color)
async def pen_selected(message: Message, state: FSMContext):
    await state.update_data(Цвет=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# ФУТБОЛКИ
@router.message(F.text == "ФУТБОЛКИ")
async def tshirts_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.tshirt_size)
    await state.update_data(Услуга="Футболки", previous_menu='souvenirs')
    await message.answer(
        "👕 ФУТБОЛКИ\n\nВыберите размер:",
        reply_markup=get_tshirt_size_keyboard()
    )

@router.message(OrderStates.tshirt_size)
async def tshirt_size_selected(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.tshirt_material)
    await message.answer(
        "Выберите материал и цвет:",
        reply_markup=get_tshirt_material_keyboard()
    )

@router.message(OrderStates.tshirt_material)
async def tshirt_material_selected(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.tshirt_print_position)
    await message.answer(
        "Выберите расположение принта:",
        reply_markup=get_tshirt_print_position_keyboard()
    )

@router.message(OrderStates.tshirt_print_position)
async def tshirt_print_position_selected(message: Message, state: FSMContext):
    await state.update_data(Позиция=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# КРУЖКИ
@router.message(F.text == "КРУЖКИ")
async def mugs_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.mug_type)
    await state.update_data(Услуга="Кружки", previous_menu='souvenirs')
    await message.answer(
        "☕ КРУЖКИ\n\nВыберите тип кружки:",
        reply_markup=get_mug_type_keyboard()
    )

@router.message(OrderStates.mug_type)
async def mug_type_selected(message: Message, state: FSMContext):
    await state.update_data(Услуга=message.text)
    await state.set_state(OrderStates.mug_print_position)
    await message.answer(
        "Выберите расположение принта:",
        reply_markup=get_mug_print_position_keyboard()
    )

@router.message(OrderStates.mug_print_position)
async def mug_print_position_selected(message: Message, state: FSMContext):
    await state.update_data(Позиция=message.text)
    await state.set_state(OrderStates.mug_packaging)
    await message.answer(
        "Выберите дополнительную упаковку:",
        reply_markup=get_mug_packaging_keyboard()
    )

@router.message(OrderStates.mug_packaging)
async def mug_packaging_selected(message: Message, state: FSMContext):
    await state.update_data(Упаковка=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )