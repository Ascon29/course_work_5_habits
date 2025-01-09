from datetime import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def perform_habits():
    """Функция-задача, которая проверяет время для выполнения полезной привычки.
    С помощью сервисной функции отправляет сообщение владельцу привычки в телеграм."""
    time_now = datetime.now()
    habits = Habit.objects.filter(is_pleasant=False)
    for habit in habits:
        if time_now.hour == habit.time.hour and time_now.minute == habit.time.minute:
            chat_id = habit.owner.tg_chat_id
            text = f"Напоминание: Вам необходимо {habit.action} в {habit.time} в {habit.place}"
            send_tg_message(chat_id=chat_id, text=text)
