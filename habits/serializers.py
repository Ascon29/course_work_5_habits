from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    """Сериализатор модели привычки."""

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidator(fields="__all__")]
