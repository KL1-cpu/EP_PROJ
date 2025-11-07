from datetime import datetime
from aiogram.types import Message
from config import RECIPIENT_ID
from utils.user_store import get_user_info  # <-- new

def create_order_message(
    username: str,
    user_id: int,
    service_type: str,
    order_data: dict,
    files_info: list = None,
    comment: str = None
) -> str:
    """Формирует сообщение о заказе для отправки менеджеру"""
    
    # Попробуем достать сохранённые ФИО/телефон
    user_info = get_user_info(user_id)
    last_name = user_info.get("last_name") if user_info else None
    first_name = user_info.get("first_name") if user_info else None
    phone = user_info.get("phone") if user_info else None

    message = f"📦 НОВЫЙ ЗАКАЗ\n\n"
    # Вставляем ФИО/телефон сверху, если есть
    if last_name or first_name or phone:
        message += "👥 Данные клиента:\n"
        if last_name or first_name:
            message += f"  • Имя: {first_name or '-'} {last_name or '-'}\n"
        if phone:
            message += f"  • Телефон: {phone}\n"
        message += "\n"

    message += f"👤 Пользователь: @{username if username else 'без username'}\n"
    # message += f"🆔 ID: {user_id}\n"
    message += f"📋 Тип услуги: {service_type}\n"
    message += f"🕒 Время заказа: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    message += "📝 Детали заказа:\n"
    for key, value in order_data.items():
        if value and value != "Пропустить" and key not in ['files_info', 'previous_menu', 'files_data']:
            formatted_key = key.replace('_', ' ').title()
            message += f"  • {formatted_key}: {value}\n"
    
    # if files_info:
    #     message += f"\n📎 Файлы ({len(files_info)}):\n"
    #     for i, file_info in enumerate(files_info, 1):
    #         clean_file_info = file_info.replace("bytes", "").replace("(", "").replace(")", "").strip()
    #         message += f"  {i}. {clean_file_info}\n"
    
    if comment and comment != "Пропустить":
        message += f"\n💬 Примечание: {comment}\n"
    
    return message

def create_order_summary(user_id: int, service_type: str, order_data: dict, files_info: list = None, comment: str = None) -> str:
	"""Краткая сводка заказа для пользователя (не полная копия сообщения менеджеру)."""
	# Получаем сохранённые ФИО/телефон если есть
	user_info = get_user_info(user_id)
	last_name = user_info.get("last_name") if user_info else None
	first_name = user_info.get("first_name") if user_info else None
	phone = user_info.get("phone") if user_info else None

	lines = []
	if first_name or last_name:
		lines.append(f"Клиент: {first_name or '-'} {last_name or '-'}")
	if phone:
		lines.append(f"Телефон: {phone}")
	lines.append(f"Услуга: {service_type}")
	# Перечислим только значимые поля из order_data
	for key, value in order_data.items():
		if value and value != "Пропустить" and key not in ['files_info', 'previous_menu', 'files_data']:
			formatted_key = key.replace('_', ' ').title()
			lines.append(f"{formatted_key}: {value}")
	# Файлы — просто кол-во, если есть
	if files_info:
		lines.append(f"Файлы: {len(files_info)}")
	# Примечание кратко
	if comment and comment != "Пропустить":
		lines.append(f"Примечание: {comment}")
	return "\n".join(lines)

async def send_order_to_manager(bot, order_message: str, files_data: list = None):
    """Отправляет заказ менеджеру по ID с файлами в одном сообщении"""
    try:
        if files_data and len(files_data) > 0:
            # Если есть файлы, отправляем первый файл с подписью-заказом
            file_data = files_data[0]
            
            if file_data['type'] == 'document':
                await bot.send_document(
                    chat_id=RECIPIENT_ID,
                    document=file_data['file_id'],
                    caption=order_message
                )
            elif file_data['type'] == 'photo':
                await bot.send_photo(
                    chat_id=RECIPIENT_ID,
                    photo=file_data['file_id'],
                    caption=order_message
                )
            
            # Остальные файлы отправляем без подписи
            for file_data in files_data[1:]:
                if file_data['type'] == 'document':
                    await bot.send_document(
                        chat_id=RECIPIENT_ID,
                        document=file_data['file_id']
                    )
                elif file_data['type'] == 'photo':
                    await bot.send_photo(
                        chat_id=RECIPIENT_ID,
                        photo=file_data['file_id']
                    )
        else:
            # Если файлов нет, отправляем просто текстовое сообщение
            await bot.send_message(chat_id=RECIPIENT_ID, text=order_message)
        
        return True
    except Exception as e:
        print(f"Ошибка отправки заказа менеджеру: {e}")
        return False