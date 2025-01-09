from rest_framework.serializers import ValidationError


class HabitValidator:
    """ Валидатор привычки. """

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value):
        if value.get('associated_habit') and value.get('reward'):
            raise ValidationError('Нельзя выбирать связанную привычку и вознаграждение одновременно')

        if value.get('time_to_complete') > 120:
            raise ValidationError('Время выполнения не может превышать 120 секунд')

        if value.get('associated_habit'):
            if not value.get('associated_habit').is_pleasant:
                raise ValidationError('Связанная привычка должна быть с признаком приятной привычки')

        if value.get('is_pleasant'):
            if value.get('associated_habit') or value.get('reward'):
                raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')

        if value.get('periodicity') > 7:
            raise ValidationError('Привычка должна выполняться не реже чем раз в 7 дней')
