from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.order_message_buttons import get_confirmed_keyboard
from keyboards.main_menu import get_main_menu_keyboard

router = Router()

@router.callback_query(F.data == "confirm")
async def confirm_order(callback: CallbackQuery):
    """Обработчик нажатия кнопки подтверждения заказа"""
    try:
        # Меняем кнопку на "Подтверждено"
        await callback.message.edit_reply_markup(reply_markup=get_confirmed_keyboard())
        
        # Получаем текст сообщения с заказом
        order_message = callback.message.caption or callback.message.text
        
        # Ищем user_id в тексте заказа
        import re
        user_id_match = re.search(r'🆔 ID: (\d+)', order_message)
        
        if user_id_match:
            user_id = int(user_id_match.group(1))
            try:
                # Получаем сохранённый ID сообщения для удаления
                from utils.user_store import get_user_info
                user_info = get_user_info(user_id)
                message_id_to_delete = user_info.get("last_confirmation_message_id") if user_info else None
                
                # Удаляем старое сообщение если есть
                if message_id_to_delete:
                    try:
                        await callback.bot.delete_message(chat_id=user_id, message_id=message_id_to_delete)
                    except Exception as e:
                        print(f"Не удалось удалить сообщение: {e}")
                
                # Отправляем новое сообщение
                await callback.bot.send_message(
                    chat_id=user_id,
                    text="✅ Менеджер ознакомился с заказом, начинаем работу",
                    reply_markup=get_main_menu_keyboard()
                )
                await callback.answer("Заказ подтвержден! Клиент уведомлен.", show_alert=False)
            except Exception as e:
                print(f"Не удалось отправить уведомление клиенту: {e}")
                await callback.answer("Заказ подтвержден, но не удалось уведомить клиента", show_alert=False)
        else:
            await callback.answer("Заказ подтвержден! ID клиента не найден.", show_alert=False)
        
    except Exception as e:
        print(f"Ошибка при подтверждении заказа: {e}")
        await callback.answer("Произошла ошибка", show_alert=True)