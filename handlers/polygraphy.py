from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from states.order_states import OrderStates
from keyboards.main_menu import get_main_menu_keyboard
from keyboards.polygraphy import *
from keyboards.copycenter import get_files_keyboard, get_comment_keyboard, get_order_confirmation_keyboard
from utils.order_message import create_order_message, send_order_to_manager

router = Router()

# Главное меню полиграфии
@router.message(F.text == "🖨️ ПОЛИГРАФИЯ")
async def polygraphy_main(message: Message, state: FSMContext):
    await state.set_state(OrderStates.waiting_for_files)
    await state.update_data(previous_menu='main')
    # Убираем старую клавиатуру
    await message.answer("Клавиатура скрыта.", reply_markup=ReplyKeyboardRemove())
    await message.answer(
        "Раздел ПОЛИГРАФИЯ. Выберите продукт:",
        reply_markup=get_polygraphy_main_keyboard()
    )

# ВИЗИТКИ
@router.message(F.text == "ВИЗИТКИ")
async def business_cards_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.business_card_print_type)
    await state.update_data(service_type="Визитки", previous_menu='polygraphy')
    await message.answer(
        "🎴 ВИЗИТКИ\n\nВыберите тип печати:",
        reply_markup=get_business_card_print_type_keyboard()
    )

# Обработчики визиток - офсетная печать
@router.message(OrderStates.business_card_print_type, F.text == "Офсетная")
async def business_cards_offset_selected(message: Message, state: FSMContext):
    await state.update_data(print_type=message.text)
    await state.set_state(OrderStates.business_card_offset_color)
    await message.answer(
        "Выберите цветность:",
        reply_markup=get_business_card_offset_color_keyboard()
    )

@router.message(OrderStates.business_card_offset_color)
async def business_cards_offset_color_selected(message: Message, state: FSMContext):
    await state.update_data(color=message.text)
    await state.set_state(OrderStates.business_card_offset_quantity)
    await message.answer(
        "Выберите количество:",
        reply_markup=get_business_card_offset_quantity_keyboard()
    )

@router.message(OrderStates.business_card_offset_quantity)
async def business_cards_offset_quantity_selected(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# Обработчики визиток - цифровая печать
@router.message(OrderStates.business_card_print_type, F.text == "Цифровая")
async def business_cards_digital_selected(message: Message, state: FSMContext):
    await state.update_data(print_type=message.text)
    await state.set_state(OrderStates.business_card_digital_paper)
    await message.answer(
        "Выберите тип бумаги:",
        reply_markup=get_business_card_digital_paper_keyboard()
    )

@router.message(OrderStates.business_card_digital_paper)
async def business_cards_digital_paper_selected(message: Message, state: FSMContext):
    await state.update_data(paper_type=message.text)
    await state.set_state(OrderStates.business_card_digital_color)
    await message.answer(
        "Выберите цветность:",
        reply_markup=get_business_card_offset_color_keyboard()  # Та же клавиатура
    )

@router.message(OrderStates.business_card_digital_color)
async def business_cards_digital_color_selected(message: Message, state: FSMContext):
    await state.update_data(color=message.text)
    await state.set_state(OrderStates.business_card_digital_lamination)
    await message.answer(
        "Выберите ламинацию:",
        reply_markup=get_business_card_digital_lamination_keyboard()
    )

@router.message(OrderStates.business_card_digital_lamination)
async def business_cards_digital_lamination_selected(message: Message, state: FSMContext):
    await state.update_data(lamination=message.text)
    await state.set_state(OrderStates.business_card_digital_quantity)
    await message.answer(
        "Выберите количество:",
        reply_markup=get_business_card_digital_quantity_keyboard()
    )

@router.message(OrderStates.business_card_digital_quantity)
async def business_cards_digital_quantity_selected(message: Message, state: FSMContext):
    await state.update_data(quantity=message.text)
    await state.set_state(OrderStates.waiting_for_files)
    await message.answer(
        "Теперь прикрепите файлы для печати:",
        reply_markup=get_files_keyboard()
    )

# БЛОКНОТЫ
@router.message(F.text == "БЛОКНОТЫ")
async def notebooks_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.notebook_format)
    await state.update_data(service_type="Блокноты", previous_menu='polygraphy')
    await message.answer(
        "📓 БЛОКНОТЫ\n\nВыберите формат:",
        reply_markup=get_notebook_format_keyboard()
    )

@router.message(OrderStates.notebook_format)
async def notebook_format_selected(message: Message, state: FSMContext):
    await state.update_data(format=message.text)
    await state.set_state(OrderStates.notebook_inner_block)
    await message.answer(
        "Выберите внутренний блок:",
        reply_markup=get_notebook_inner_block_keyboard()
    )

@router.message(OrderStates.notebook_inner_block)
async def notebook_inner_block_selected(message: Message, state: FSMContext):
    await state.update_data(inner_block=message.text)
    await state.set_state(OrderStates.notebook_cover_type)
    await message.answer(
        "Выберите тип обложки:",
        reply_markup=get_notebook_cover_type_keyboard()
    )

@router.message(OrderStates.notebook_cover_type)
async def notebook_cover_type_selected(message: Message, state: FSMContext):
    await state.update_data(cover_type=message.text)
    await state.set_state(OrderStates.notebook_backing)
    await message.answer(
        "Выберите подложку:",
        reply_markup=get_notebook_backing_keyboard()
    )

@router.message(OrderStates.notebook_backing)
async def notebook_backing_selected(message: Message, state: FSMContext):
    await state.update_data(backing=message.text)
    await state.set_state(OrderStates.notebook_stitching)
    await message.answer(
        "Выберите позицию сшивания:",
        reply_markup=get_notebook_stitching_keyboard()
    )

@router.message(OrderStates.notebook_stitching)
async def notebook_stitching_selected(message: Message, state: FSMContext):
    await state.update_data(stitching=message.text)
    await state.set_state(OrderStates.notebook_pages)
    await message.answer(
        "Выберите количество страниц:",
        reply_markup=get_notebook_pages_keyboard()
    )

@router.message(OrderStates.notebook_pages)
async def notebook_pages_selected(message: Message, state: FSMContext):
    await state.update_data(pages=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# БУКЛЕТЫ
@router.message(F.text == "БУКЛЕТЫ")
async def booklets_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.booklet_format)
    await state.update_data(service_type="Буклеты", previous_menu='polygraphy')
    await message.answer(
        "📰 БУКЛЕТЫ\n\nВыберите формат готового изделия:",
        reply_markup=get_booklet_format_keyboard()
    )

@router.message(OrderStates.booklet_format)
async def booklet_format_selected(message: Message, state: FSMContext):
    await state.update_data(format=message.text)
    await state.set_state(OrderStates.booklet_paper_type)
    await message.answer(
        "Выберите тип бумаги:",
        reply_markup=get_booklet_paper_type_keyboard()
    )

@router.message(OrderStates.booklet_paper_type)
async def booklet_paper_type_selected(message: Message, state: FSMContext):
    await state.update_data(paper_type=message.text)
    await state.set_state(OrderStates.booklet_color)
    await message.answer(
        "Выберите цветность:",
        reply_markup=get_booklet_color_keyboard()
    )

@router.message(OrderStates.booklet_color)
async def booklet_color_selected(message: Message, state: FSMContext):
    await state.update_data(color=message.text)
    await state.set_state(OrderStates.booklet_fold_type)
    await message.answer(
        "Выберите тип сгиба:",
        reply_markup=get_booklet_fold_type_keyboard()
    )

@router.message(OrderStates.booklet_fold_type)
async def booklet_fold_type_selected(message: Message, state: FSMContext):
    await state.update_data(fold_type=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# КАЛЕНДАРИ
@router.message(F.text == "КАЛЕНДАРИ")
async def calendars_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.calendar_type)
    await state.update_data(service_type="Календари", previous_menu='polygraphy')
    await message.answer(
        "📅 КАЛЕНДАРИ\n\nВыберите вид календаря:",
        reply_markup=get_calendar_type_keyboard()
    )

@router.message(OrderStates.calendar_type)
async def calendar_type_selected(message: Message, state: FSMContext):
    await state.update_data(calendar_type=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# КОНВЕРТЫ
@router.message(F.text == "КОНВЕРТЫ")
async def envelopes_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.envelope_type)
    await state.update_data(service_type="Конверты", previous_menu='polygraphy')
    await message.answer(
        "✉️ КОНВЕРТЫ\n\nВыберите тип конверта:",
        reply_markup=get_envelope_type_keyboard()
    )

@router.message(OrderStates.envelope_type)
async def envelope_type_selected(message: Message, state: FSMContext):
    await state.update_data(envelope_type=message.text)
    await state.set_state(OrderStates.waiting_for_quantity)
    await message.answer(
        "Введите количество экземпляров:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[[KeyboardButton(text="🏠 Главное меню")]],
            resize_keyboard=True
        )
    )

# Обработчики для остальных продуктов полиграфии (схема аналогична)
@router.message(F.text == "ЛИСТОВКИ")
async def leaflets_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.leaflet_format)
    await state.update_data(service_type="Листовки", previous_menu='polygraphy')
    await message.answer(
        "📄 ЛИСТОВКИ\n\nВыберите формат:",
        reply_markup=get_leaflet_format_keyboard()
    )

@router.message(F.text == "ПЕЧАТЬ НА САМОКЛЕЙКЕ")
async def stickers_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.sticker_material_type)
    await state.update_data(service_type="Печать на самоклейке", previous_menu='polygraphy')
    await message.answer(
        "🏷️ ПЕЧАТЬ НА САМОКЛЕЙКЕ\n\nВыберите тип материала:",
        reply_markup=get_sticker_material_type_keyboard()
    )

@router.message(F.text == "ПЛАКАТЫ")
async def posters_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.poster_format)
    await state.update_data(service_type="Плакаты", previous_menu='polygraphy')
    await message.answer(
        "📊 ПЛАКАТЫ\n\nВыберите формат:",
        reply_markup=get_poster_format_keyboard()
    )

@router.message(F.text == "СЕРТИФИКАТЫ")
async def certificates_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.certificate_format)
    await state.update_data(service_type="Сертификаты", previous_menu='polygraphy')
    await message.answer(
        "🏆 СЕРТИФИКАТЫ\n\nВыберите формат:",
        reply_markup=get_certificate_format_keyboard()
    )

@router.message(F.text == "СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ")
async def sticker_packs_start(message: Message, state: FSMContext):
    await state.set_state(OrderStates.sticker_pack_material)
    await state.update_data(service_type="Стикеры с плоттерной резкой", previous_menu='polygraphy')
    await message.answer(
        "🔖 СТИКЕРЫ С ПЛОТТЕРНОЙ РЕЗКОЙ\n\nВыберите тип материала:",
        reply_markup=get_sticker_pack_material_keyboard()
    )

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
    
    success = await send_order_to_manager(message.bot, order_message)
    
    # Скрываем старую клавиатуру и показываем inline-меню
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