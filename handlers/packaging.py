from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.packaging import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Главное меню упаковки
@router.message(F.text == "📦 УПАКОВКА")
async def packaging_main(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    await message.answer(
        "Раздел УПАКОВКА. Выберите продукт:",
        reply_markup=get_packaging_main_keyboard()
    )

# ПАКЕТЫ БУМАЖНЫЕ
@router.message(F.text == "ПАКЕТЫ")
async def bags_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.bag_type)
    await state.update_data(Услуга="Пакеты", previous_menu='packaging')
    await message.answer(
        "🛍️ ПАКЕТЫ\n\nВыберите тип пакета:",
        reply_markup=get_bag_type_keyboard()
    )

# Обработчики бумажных пакетов
@router.message(OrderStates.bag_type, F.text == "Бумажные пакеты")
async def paper_bags_selected(message: Message, state: FSMContext):
    await state.update_data(Услуга=message.text)
    await state.set_state(OrderStates.bag_paper_print)
    await message.answer(
        "Выберите тип печати:",
        reply_markup=get_bag_paper_print_keyboard()
    )

@router.message(OrderStates.bag_paper_print)
async def paper_bags_print_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_печати=message.text)
    await state.set_state(OrderStates.bag_paper_format)
    await message.answer(
        "Выберите формат пакета:",
        reply_markup=get_bag_paper_format_keyboard()
    )

@router.message(OrderStates.bag_paper_format)
async def paper_bags_format_selected(message: Message, state: FSMContext):
    await state.update_data(Формат=message.text)
    await state.set_state(OrderStates.bag_paper_lamination)
    await message.answer(
        "Выберите ламинированное покрытие:",
        reply_markup=get_bag_paper_lamination_keyboard()
    )

@router.message(OrderStates.bag_paper_lamination)
async def paper_bags_lamination_selected(message: Message, state: FSMContext):
    await state.update_data(Ламинация=message.text)
    await state.set_state(OrderStates.bag_paper_grommets)
    await message.answer(
        "Выберите люверсы:",
        reply_markup=get_bag_paper_grommets_keyboard()
    )

@router.message(OrderStates.bag_paper_grommets)
async def paper_bags_grommets_selected(message: Message, state: FSMContext):
    await state.update_data(Люверсы=message.text)
    await state.set_state(OrderStates.bag_paper_handle)
    await message.answer(
        "Выберите ручку-шнурок:",
        reply_markup=get_bag_paper_handle_keyboard()
    )

@router.message(OrderStates.bag_paper_handle)
async def paper_bags_handle_selected(message: Message, state: FSMContext):
    await state.update_data(Ручка=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# Обработчики ПВД пакетов
@router.message(OrderStates.bag_type, F.text == "ПВД пакеты")
async def pvd_bags_selected(message: Message, state: FSMContext):
    await state.update_data(Услуга=message.text)
    await state.set_state(OrderStates.bag_pvd_print)
    await message.answer(
        "Выберите печать:",
        reply_markup=get_bag_pvd_print_keyboard()
    )

@router.message(OrderStates.bag_pvd_print)
async def pvd_bags_print_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_печати=message.text)
    await state.set_state(OrderStates.bag_pvd_format)
    await message.answer(
        "Выберите формат:",
        reply_markup=get_bag_pvd_format_keyboard()
    )

@router.message(OrderStates.bag_pvd_format)
async def pvd_bags_format_selected(message: Message, state: FSMContext):
    await state.update_data(Формат=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# КОРОБКИ
@router.message(F.text == "КОРОБКИ")
async def boxes_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.box_material)
    await state.update_data(Услуга="Коробки", previous_menu='packaging')
    await message.answer(
        "📦 КОРОБКИ\n\nВыберите материал коробки:",
        reply_markup=get_box_material_keyboard()
    )

# Обработчики коробок из мелованного картона
@router.message(OrderStates.box_material, F.text == "Коробки из мелованного картона")
async def cardboard_boxes_selected(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.box_cardboard_size)
    await message.answer(
        "Введите размеры коробки в формате Д×Ш×В (мм):",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.box_cardboard_size)
async def cardboard_boxes_size_entered(message: Message, state: FSMContext):
    await state.update_data(Размер=message.text)
    await state.set_state(OrderStates.box_cardboard_print)
    await message.answer(
        "Выберите печать на коробке:",
        reply_markup=get_box_cardboard_print_keyboard()
    )

@router.message(OrderStates.box_cardboard_print)
async def cardboard_boxes_print_selected(message: Message, state: FSMContext):
    await state.update_data(Печать=message.text)
    await state.set_state(OrderStates.box_cardboard_lamination)
    await message.answer(
        "Выберите ламинированное покрытие:",
        reply_markup=get_bag_paper_lamination_keyboard()  # Та же клавиатура
    )

@router.message(OrderStates.box_cardboard_lamination)
async def cardboard_boxes_lamination_selected(message: Message, state: FSMContext):
    await state.update_data(Ламинирование=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# Обработчики коробок из микро-гофры
@router.message(OrderStates.box_material, F.text == "Коробки из микро-гофры")
async def corrugated_boxes_selected(message: Message, state: FSMContext):
    await state.update_data(Материал=message.text)
    await state.set_state(OrderStates.box_corrugated_format)
    await message.answer(
        "Выберите формат коробки:",
        reply_markup=get_box_corrugated_format_keyboard()
    )

@router.message(OrderStates.box_corrugated_format)
async def corrugated_boxes_format_selected(message: Message, state: FSMContext):
    await state.update_data(Формат=message.text)
    await state.set_state(OrderStates.box_corrugated_color)
    await message.answer(
        "Выберите цвет микрогофры:",
        reply_markup=get_box_corrugated_color_keyboard()
    )

@router.message(OrderStates.box_corrugated_color)
async def corrugated_boxes_color_selected(message: Message, state: FSMContext):
    await state.update_data(Цвет=message.text)
    await state.set_state(OrderStates.box_corrugated_logo)
    await message.answer(
        "Выберите нанесение логотипа:",
        reply_markup=get_box_corrugated_logo_keyboard()
    )

@router.message(OrderStates.box_corrugated_logo)
async def corrugated_boxes_logo_selected(message: Message, state: FSMContext):
    await state.update_data(Логотип=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.callback_query(F.data == "confirm_order")
async def confirm_order(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    order_message = create_order_message(
        username=callback.from_user.username,
        user_id=callback.from_user.id,
        service_type=data.get('service_type', 'Неизвестная услуга'),
        order_data=data,
        files_info=data.get('files_info', []),
        comment=data.get('comment')
    )
    success = await send_order_to_manager(callback.bot, order_message)
    
    # Убираем старую ReplyKeyboard, затем отправляем пользователю сводку и финальное сообщение с inline-меню
    await callback.answer()
    await callback.message.answer("Клавиатура скрыта.", reply_markup=ReplyKeyboardRemove())
    await callback.message.answer("Вот ваш заказ (копия):")
    await callback.message.answer(order_message)
    
    if success:
        await callback.message.edit_text(
            "✅ Ваш заказ успешно отправлен менеджеру!\nС вами свяжутся в ближайшее время для уточнения деталей.",
            reply_markup=get_main_menu_keyboard()
        )
    else:
        await callback.message.edit_text(
            "❌ Произошла ошибка при отправке заказа. Пожалуйста, попробуйте позже.",
            reply_markup=get_main_menu_keyboard()
        )
    await state.clear()