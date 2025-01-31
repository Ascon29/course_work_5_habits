from rest_framework import generics

from habits.models import Habit
from habits.paginations import HabitsPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitUserListAPIView(generics.ListAPIView):
    """Контроллер отображения списка привычек авторизованного пользователя."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Контроллер отображения списка публичных привычек."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер отображения информации о привычке."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super().get_permissions()


class HabitCreateAPIView(generics.CreateAPIView):
    """Контроллер создания привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Контроллер обновления привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super().get_permissions()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Контроллер удаления привычки."""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer

    def get_permissions(self):
        self.permission_classes = [IsOwner]
        return super().get_permissions()
