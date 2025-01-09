from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""

    username = None
    email = models.EmailField(unique=True, verbose_name="почта", help_text="Введите почту")
    last_name = models.CharField(
        max_length=100, verbose_name="фамилия", help_text="Введите фамилию", blank=True, null=True
    )
    first_name = models.CharField(max_length=100, verbose_name="имя", help_text="Введите имя", blank=True, null=True)
    tg_chat_id = models.CharField(
        max_length=50, verbose_name="Телеграмм chat_id", help_text="Введите телеграмм chat_id", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.email}"
