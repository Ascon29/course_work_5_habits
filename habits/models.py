from django.db import models

from config import settings


class Habit(models.Model):
    """Модель привычки."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="владелец", blank=True, null=True
    )
    place = models.CharField(
        max_length=255, verbose_name="место выполнения", help_text="введите место для выполнения привычки"
    )
    time = models.TimeField(verbose_name="время выполнения", help_text="введите время выполнения привычки")
    action = models.TextField(verbose_name="действие привычки", help_text="введите действие привычки")
    is_pleasant = models.BooleanField(
        default=False, verbose_name="признак приятной привычки", help_text="укажите признак приятной привычки"
    )
    associated_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="связанная привычка",
        blank=True,
        null=True,
        help_text="укажите связанную привычку",
    )
    reward = models.CharField(
        max_length=255,
        verbose_name="вознаграждение",
        help_text="введите вознаграждение за выполнение привычки",
        blank=True,
        null=True,
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name="периодичность выполнения",
        help_text="введите периодичность выполнения привычки в днях (по умолчанию 1)",
    )
    time_to_complete = models.PositiveIntegerField(
        default=120, verbose_name="время на выполнение", help_text="введите время на выполнение"
    )
    is_public = models.BooleanField(
        default=False, verbose_name="признак публичность", help_text="введите признак публичности"
    )

    class Meta:
        verbose_name = ("привычка",)
        verbose_name_plural = "привычки"

    def __str__(self):
        return f"Я буду {self.action}, в {self.place}, в {self.time}"
