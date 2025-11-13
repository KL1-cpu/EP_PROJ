from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.copycenter import (
    get_copycenter_main_keyboard,
    get_bw_format_keyboard,
    get_bw_print_type_keyboard,
    get_bw_additional_services_keyboard,
    get_color_format_keyboard,
    get_color_paper_type_keyboard,
    get_color_additional_services_keyboard,
    get_files_keyboard,
    get_comment_keyboard,
    get_order_confirmation_keyboard,
    get_risograph_format_keyboard,
    get_risograph_quantity_keyboard,
    get_risograph_color_keyboard,
    get_risograph_print_type_keyboard
)
from utils.order_message import create_order_message, send_order_to_manager, create_order_summary  # <-- added

router = Router()

# Обработчики главного меню копицентра
@router.message(F.text == "📄 КОПИЦЕНТР")
async def copycenter_main(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    # Убираем старую клавиатуру перед показом inline-меню
    await message.answer("Клавиатура скрыта.", reply_markup=ReplyKeyboardRemove())
    await message.answer(
        "Раздел КОПИЦЕНТР. Выберите тип печати:",
        reply_markup=get_copycenter_main_keyboard()
    )

@router.message(F.text == "Ч/Б ПЕЧАТЬ")
async def bw_print_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.bw_format)
    await state.update_data(Услуга="Ч/Б печать", previous_menu='copycenter')
    await message.answer(
        "🖨️ Ч/Б ПЕЧАТЬ\n\n"
        "Выберите формат:",
        reply_markup=get_bw_format_keyboard()
    )

@router.message(F.text == "ЦВЕТНАЯ ПЕЧАТЬ")
async def color_print_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.color_format)
    await state.update_data(Услуга="Цветная печать", previous_menu='copycenter')
    await message.answer(
        "🎨 ЦВЕТНАЯ ПЕЧАТЬ\n\n"
        "Выберите формат:",
        reply_markup=get_color_format_keyboard()
    )

# Обработчики Ч/Б печати
@router.message(OrderStates.bw_format, F.text.in_(["A4", "A3"]))
async def bw_format_selected(message: Message, state: FSMContext):
    await state.update_data(Формат=message.text)
    await state.set_state(OrderStates.bw_print_type)
    await message.answer(
        "Выберите тип печати:",
        reply_markup=get_bw_print_type_keyboard()
    )

@router.message(OrderStates.bw_print_type, F.text.in_(["Односторонняя", "Двусторонняя", "Печать брошюры"]))
async def bw_print_type_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_печати=message.text)
    await state.set_state(OrderStates.bw_additional_services)
    await message.answer(
        "Выберите дополнительные услуги:",
        reply_markup=get_bw_additional_services_keyboard()
    )

@router.message(OrderStates.bw_additional_services)
async def bw_additional_services_selected(message: Message, state: FSMContext):
    if message.text != "Пропустить":
        await state.update_data(additional_services=message.text)
    
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# Обработчики цветной печати
@router.message(OrderStates.color_format, F.text.in_([
    "A7 (74×105 мм)", "A6 (105×148 мм)", "Евроформат (210×99 мм)", 
    "A5 (148×210 мм)", "A4 (210×297 мм)", "A3 (297×420 мм)"
]))
async def color_format_selected(message: Message, state: FSMContext):
    await state.update_data(Формат=message.text)
    await state.set_state(OrderStates.color_paper_type)
    await message.answer(
        "Выберите тип бумаги:",
        reply_markup=get_color_paper_type_keyboard()
    )

@router.message(OrderStates.color_paper_type)
async def color_paper_type_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_бумаги=message.text)
    await state.set_state(OrderStates.color_print_type)
    await message.answer(
        "Выберите тип печати:",
        reply_markup=get_bw_print_type_keyboard()  # Та же клавиатура, что и для Ч/Б
    )

@router.message(OrderStates.color_print_type, F.text.in_(["Односторонняя", "Двусторонняя", "Печать брошюры"]))
async def color_print_type_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_печати=message.text)
    await state.set_state(OrderStates.color_additional_services)
    await message.answer(
        "Выберите дополнительные услуги:",
        reply_markup=get_color_additional_services_keyboard()
    )

@router.message(OrderStates.color_additional_services)
async def color_additional_services_selected(message: Message, state: FSMContext):
    if message.text != "Пропустить":
        await state.update_data(Доп_услуги=message.text)
    
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# Обработчик количества
@router.message(OrderStates.waiting_for_quantity, F.text.regexp(r'^\d+$'))
async def quantity_entered(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# Обработчик файлов
# @router.message(OrderStates.waiting_for_files, F.text == "📎 Прикрепить файлы")
# async def request_files(message: Message, state: FSMContext):
#     await message.answer(
#         "Пожалуйста, прикрепите файлы (документы или изображения):",
#         reply_markup=ReplyKeyboardMarkup(
#             keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
#             resize_keyboard=True
#         )
#     )

@router.message(OrderStates.waiting_for_files, F.document | F.photo)
async def files_received(message: Message, state: FSMContext):
    files_info = []
    
    if message.document:
        file_info = f"📄 {message.document.file_name} ({message.document.file_size} bytes)"
        files_info.append(file_info)
    elif message.photo:
        photo = message.photo[-1]
        file_info = f"🖼️ Фото ({photo.file_size} bytes)"
        files_info.append(file_info)
    
    await state.update_data(files_info=files_info)
    await state.set_state(OrderStates.waiting_for_comment)
    await message.answer(
        "Файлы получены! Хотите добавить примечание к заказу?",
        reply_markup=get_comment_keyboard()
    )

# Обработчик примечания
@router.message(OrderStates.waiting_for_comment, F.text == "📝 Добавить примечание")
async def request_comment(message: Message, state: FSMContext):
    await message.answer(
        "Введите примечание к заказу:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.waiting_for_comment)
async def comment_received(message: Message, state: FSMContext):
    if message.text not in ["Пропустить", "⬅️ Назад", "🏠 Главное меню"]:
        await state.update_data(comment=message.text)
    
    # Переходим к подтверждению заказа
    data = await state.get_data()
    Услуга = data.get('service_type', 'Неизвестная услуга')

    # Краткая сводка
    summary = create_order_summary(message.from_user.id, Услуга, data, files_info=data.get('files_info', []), comment=data.get('comment'))

    await state.set_state(OrderStates.waiting_for_files)  # Сброс состояния
    await message.answer(
        f"Заказ {Услуга} готов к отправке!\n\n"
        f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
        reply_markup=get_order_confirmation_keyboard()
    )

# Обработчик подтверждения заказа
@router.message(F.text == "✅ Отправить заказ-подтверждение")
async def confirm_order(message: Message, state: FSMContext):
    data = await state.get_data()
    
    order_message = create_order_message(
        username=message.from_user.username,
        user_id=message.from_user.id,
        service_type=data.get('service_type', 'Неизвестная услуга'),
        order_data=data,
        files_info=data.get('files_info', []),
        comment=data.get('comment')
    )
    
    # Отправляем менеджеру
    success = await send_order_to_manager(message.bot, order_message)
    
    # Убираем старую клавиатуру и показываем inline главное меню вместе с результатом
    await message.answer("Клавиатура скрыта.", reply_markup=ReplyKeyboardRemove())
    await message.answer("Вот ваш заказ (копия):")
    await message.answer(order_message)
    
    if success:
        await message.answer(
            "✅ Ваш заказ успешно отправлен менеджеру!\n"
            "С вами свяжутся в ближайшее время для уточнения деталей.",
            reply_markup=get_main_menu_keyboard()
        )
    else:
        await message.answer(
            "❌ Произошла ошибка при отправке заказа. Пожалуйста, попробуйте позже.",
            reply_markup=get_main_menu_keyboard()
        )
    
    await state.clear()

# РИЗОГРАФ
@router.message(F.text == "РИЗОГРАФ")
async def risograph_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.risograph_format)
    await state.update_data(Услуга="Ризограф", previous_menu='copycenter')
    await message.answer(
        "🖨️ РИЗОГРАФ\n\nВыберите формат:",
        reply_markup=get_risograph_format_keyboard()
    )

@router.message(OrderStates.risograph_format, F.text.in_(["A4", "А3"]))
async def risograph_format_selected(message: Message, state: FSMContext):
    await state.update_data(Формат=message.text)
    await state.set_state(OrderStates.risograph_quantity)
    await message.answer(
        "Выберите количество экземпляров:",
        reply_markup=get_risograph_quantity_keyboard()
    )

@router.message(OrderStates.risograph_quantity)
async def risograph_quantity_selected(message: Message, state: FSMContext):
    await state.update_data(Количество=message.text)
    await state.set_state(OrderStates.risograph_color)
    await message.answer(
        "Выберите цвет печати:",
        reply_markup=get_risograph_color_keyboard()
    )

@router.message(OrderStates.risograph_color)
async def risograph_color_selected(message: Message, state: FSMContext):
    await state.update_data(Цвет=message.text)
    await state.set_state(OrderStates.risograph_print_type)
    await message.answer(
        "Выберите тип печати:",
        reply_markup=get_risograph_print_type_keyboard()
    )

@router.message(OrderStates.risograph_print_type)
async def risograph_print_type_selected(message: Message, state: FSMContext):
    await state.update_data(Тип_печати=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )