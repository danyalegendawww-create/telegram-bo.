import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ADMIN_IDS = [
    7647772048,  # Админ
    7414039324   # Разработчик
]

MOSCOW_TIMEZONE = "Europe/Moscow"
