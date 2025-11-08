from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.interior import *
from keyboards.polygraphy import get_poster_format_keyboard, get_poster_paper_type_a3_keyboard, get_poster_paper_type_large_keyboard, get_poster_cutting_keyboard
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Главное меню интерьерной печати
@router.message(F.text == "🖼️ ИНТЕРЬЕРНАЯ ПЕЧАТЬ")
async def interior_main(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await message.answer(
        "Раздел ИНТЕРЬЕРНАЯ ПЕЧАТЬ. Выберите продукт:",
        reply_markup=get_interior_main_keyboard()
    )

# ПЛАКАТЫ (дублирует полиграфию)
@router.message(F.text == "ПЛАКАТЫ")
async def interior_posters_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.interior_poster_format)
    await state.update_data(Услуга="Интерьерные плакаты", previous_menu='interior')
    await message.answer(
        "📊 ИНТЕРЬЕРНЫЕ ПЛАКАТЫ\n\nВыберите формат:",
        reply_markup=get_poster_format_keyboard()
    )

# ТАБЛИЧКИ
@router.message(F.text == "ТАБЛИЧКИ")
async def signs_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.sign_type)
    await state.update_data(Услуга="Таблички", previous_menu='interior')
    await message.answer(
        "🏢 ТАБЛИЧКИ\n\nВыберите тип таблички:",
        reply_markup=get_sign_type_keyboard()
    )

@router.message(OrderStates.sign_type)
async def sign_type_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_таблички=message.text)
    await state.set_state(OrderStates.sign_size)
    await message.answer(
        "Введите размер таблички в формате Ш×В (мм):",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.sign_size)
async def sign_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.sign_material)
    await message.answer(
        "Выберите материал:",
        reply_markup=get_sign_material_keyboard()
    )

@router.message(OrderStates.sign_material)
async def sign_material_selected(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# КАРТИНЫ НА ХОЛСТЕ
@router.message(F.text == "КАРТИНЫ НА ХОЛСТЕ")
async def canvas_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.canvas_size)
    await state.update_data(Услуга="Картины на холсте", previous_menu='interior')
    await message.answer(
        "🎨 КАРТИНЫ НА ХОЛСТЕ\n\nВыберите размер холста:",
        reply_markup=get_canvas_size_keyboard()
    )

@router.message(OrderStates.canvas_size)
async def canvas_size_selected(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.canvas_framing)
    await message.answer(
        "Выберите оформление:",
        reply_markup=get_canvas_framing_keyboard()
    )

@router.message(OrderStates.canvas_framing)
async def canvas_framing_selected(message: Message, state: FSMContext):
    await state.update_data(Оформление=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# ПЕЧАТЬ НА БАННЕРЕ
@router.message(F.text == "ПЕЧАТЬ НА БАННЕРЕ")
async def banner_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.banner_print_type)
    await state.update_data(Услуга="Печать на баннере", previous_menu='interior')
    await message.answer(
        "🪧 ПЕЧАТЬ НА БАННЕРЕ\n\nВыберите тип печати:",
        reply_markup=get_banner_print_type_keyboard()
    )

@router.message(OrderStates.banner_print_type)
async def banner_print_type_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_печати=message.text)
    await state.set_state(OrderStates.banner_size)
    await message.answer(
        "Введите размер баннера в формате Ш×В (мм):",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.banner_size)
async def banner_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.banner_edge_processing)
    await message.answer(
        "Выберите обработку краев:",
        reply_markup=get_banner_edge_processing_keyboard()
    )

@router.message(OrderStates.banner_edge_processing, F.text == "Укрепление края")
async def banner_edge_processing_selected(message: Message, state: FSMContext):
    await state.update_data(Края=message.text)
    await state.set_state(OrderStates.banner_grommets)
    await message.answer(
        "Выберите крепление:",
        reply_markup=get_banner_grommets_keyboard()
    )

@router.message(OrderStates.banner_grommets)
async def banner_grommets_selected(message: Message, state: FSMContext):
    await state.update_data(Крепление=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.banner_edge_processing, F.text == "Без обработки")
async def banner_no_processing_selected(message: Message, state: FSMContext):
    await state.update_data(Края=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ
@router.message(F.text == "ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ")
async def interior_stickers_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.interior_sticker_film_type)
    await state.update_data(Услуга="Печать на самоклеющейся плёнке", previous_menu='interior')
    await message.answer(
        "🏷️ ПЕЧАТЬ НА САМОКЛЕЮЩЕЙСЯ ПЛЁНКЕ\n\nВыберите тип плёнки:",
        reply_markup=get_interior_sticker_film_type_keyboard()
    )

@router.message(OrderStates.interior_sticker_film_type)
async def interior_sticker_film_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_плёнки=message.text)
    await state.set_state(OrderStates.interior_sticker_size)
    await message.answer(
        "Введите размер в формате Ш×В (мм):",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.interior_sticker_size)
async def interior_sticker_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.interior_sticker_processing)
    await message.answer(
        "Выберите дополнительную обработку:",
        reply_markup=get_interior_sticker_processing_keyboard()
    )

@router.message(OrderStates.interior_sticker_processing)
async def interior_sticker_processing_selected(message: Message, state: FSMContext):
    await state.update_data(Доп_обработка=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )