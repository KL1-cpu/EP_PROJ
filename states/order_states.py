from aiogram.fsm.state import State, StatesGroup
from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.context import FSMContext


from keyboards.main_menu import get_main_menu_keyboard
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager, create_order_summary

router = Router()

class OrderStates(StatesGroup):
    # Общие состояния
    waiting_for_files = State()
    waiting_for_comment = State()
    waiting_for_quantity = State()
    
    # Копицентр - Ч/Б печать
    bw_format = State()
    bw_print_type = State()
    bw_additional_services = State()
    
    # Копицентр - Цветная печать
    color_format = State()
    color_paper_type = State()
    color_print_type = State()
    color_additional_services = State()
    
    # Полиграфия - Визитки
    business_card_print_type = State()
    business_card_offset_color = State()
    business_card_offset_quantity = State()
    business_card_digital_paper = State()
    business_card_digital_color = State()
    business_card_digital_lamination = State()
    business_card_digital_quantity = State()
    
    # Полиграфия - Блокноты
    notebook_format = State()
    notebook_inner_block = State()
    notebook_cover_type = State()
    notebook_backing = State()
    notebook_stitching = State()
    notebook_pages = State()
    
    # Полиграфия - Буклеты
    booklet_format = State()
    booklet_paper_type = State()
    booklet_color = State()
    booklet_fold_type = State()
    
    # Полиграфия - Календари
    calendar_type = State()
    
    # Полиграфия - Конверты
    envelope_type = State()
    
    # Полиграфия - Листовки
    leaflet_format = State()
    leaflet_paper_type = State()
    leaflet_color = State()
    
    # Полиграфия - Печать на самоклейке
    sticker_material_type = State()
    sticker_print_format = State()
    sticker_cutting = State()
    
    # Полиграфия - Плакаты
    poster_format = State()
    poster_paper_type_a3 = State()
    poster_cutting_a3 = State()
    poster_paper_type_large = State()
    poster_cutting_large = State()
    
    # Полиграфия - Сертификаты
    certificate_format = State()
    certificate_paper_type = State()
    certificate_color = State()
    certificate_lamination = State()
    
    # Полиграфия - Стикеры
    sticker_pack_material = State()
    sticker_pack_format = State()
    sticker_pack_color = State()
    sticker_pack_cutting = State()
    
    # Упаковка - Пакеты
    bag_type = State()
    bag_paper_print = State()
    bag_paper_format = State()
    bag_paper_lamination = State()
    bag_paper_grommets = State()
    bag_paper_handle = State()
    bag_pvd_print = State()
    bag_pvd_format = State()
    
    # Упаковка - Коробки
    box_material = State()
    box_cardboard_size = State()
    box_cardboard_print = State()
    box_cardboard_lamination = State()
    box_corrugated_format = State()
    box_corrugated_color = State()
    box_corrugated_logo = State()
    
    # Интерьерная печать - Плакаты (дублирует полиграфию)
    interior_poster_format = State()
    
    # Интерьерная печать - Таблички
    sign_type = State()
    sign_size = State()
    sign_material = State()
    
    # Интерьерная печать - Картины на холсте
    canvas_size = State()
    canvas_framing = State()
    
    # Интерьерная печать - Печать на баннере
    banner_print_type = State()
    banner_size = State()
    banner_edge_processing = State()
    banner_grommets = State()
    
    # Интерьерная печать - Печать на самоклейке
    interior_sticker_film_type = State()
    interior_sticker_size = State()
    interior_sticker_processing = State()
    
    # Сувениры - Ручки
    pen_material = State()
    pen_color = State()
    pen_application = State()
    
    # Сувениры - Футболки
    tshirt_size = State()
    tshirt_material = State()
    tshirt_print_position = State()
    
    # Сувениры - Кружки
    mug_type = State()
    mug_print_position = State()
    mug_packaging = State()
    
    # Печати и штампы
    stamp_type = State()
    stamp_format = State()
    stamp_ink_color = State()
    
    # Фотопечать
    photo_format = State()
    photo_print_type = State()
    
    # ФИО/регистрация пользователя
    registration_last_name = State()
    registration_first_name = State()
    registration_phone = State()

# Добавить в конец файла states/order_states.py

@router.message(OrderStates.waiting_for_quantity, F.text.regexp(r'^\d+$'))
async def quantity_entered(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы:",
        reply_markup=get_files_keyboard()
    )

@router.message(OrderStates.waiting_for_files, F.text == "📎 Прикрепить файлы")
async def request_files(message: Message, state: FSMContext):
    await message.answer(
        "Пожалуйста, прикрепите файлы (документы или изображения):",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

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
    
    # Сохраняем информацию о файлах
    current_data = await state.get_data()
    existing_files = current_data.get('files_info', [])
    existing_files.extend(files_info)
    await state.update_data(files_info=existing_files)
    
    await message.answer(
        f"Файл получен! Всего файлов: {len(existing_files)}\n"
        "Можете прикрепить еще файлы или перейти к следующему шагу.",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="📎 Прикрепить еще файлы")],
                [KeyboardButton(text="📝 Добавить примечание")],
                [KeyboardButton(text="✅ Отправить заказ-подтверждение")],
                [KeyboardButton(text="🏠 Главное меню")]
            ],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.waiting_for_comment)
async def request_comment(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_comment)
    await message.answer(
        "Введите примечание к заказу:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="Пропустить")],
                     [KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

@router.message(OrderStates.waiting_for_comment)
async def comment_received(message: Message, state: FSMContext):
    if message.text != "Пропустить":
        await state.update_data(comment=message.text)
    
    # Переходим к подтверждению заказа
    data = await state.get_data()
    service_type = data.get('service_type', 'Неизвестная услуга')

    # Краткая сводка
    summary = create_order_summary(message.from_user.id, service_type, data, files_info=data.get('files_info', []), comment=data.get('comment'))

    await message.answer(
        f"Заказ {service_type} готов к отправке!\n\n"
        f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
        reply_markup=get_order_confirmation_keyboard()
    )

@router.message(OrderStates.waiting_for_comment, F.text == "Пропустить")
async def skip_comment(message: Message, state: FSMContext):
    data = await state.get_data()
    service_type = data.get('service_type', 'Неизвестная услуга')

    # Краткая сводка
    summary = create_order_summary(message.from_user.id, service_type, data, files_info=data.get('files_info', []), comment=data.get('comment'))

    await message.answer(
        f"Заказ {service_type} готов к отправке!\n\n"
        f"Проверьте детали заказа и нажмите кнопку для отправки менеджеру:\n\n{summary}",
        reply_markup=get_order_confirmation_keyboard()
    )

@router.message(F.text == "✅ Отправить заказ-подтверждение")
async def confirm_order(message: Message, state: FSMContext):
    data = await state.get_data()
    
    # Формируем сообщение заказа
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
    
    # Отправляем пользователю копию заказа
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