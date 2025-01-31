import requests

from config import settings


def send_tg_message(chat_id, text):
    """Функция отправки сообщения в телеграм."""
    params = {"chat_id": chat_id, "text": text}
    requests.get(f"{settings.TG_URL}{settings.TG_BOT_TOKEN}/sendMessage", params=params)
