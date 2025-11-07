import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
# ИЗМЕНЕНИЕ: отправляем по ID вместо username
RECIPIENT_ID = 627160379  # ID получателя

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения")