from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Контроллер создания пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """Контроллер отображения списка пользователей."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    """Контроллер просмотра информации о пользователе."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    """Контроллер обновления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPIView(DestroyAPIView):
    """Контроллер удаления пользователя."""

    queryset = User.objects.all()
    serializer_class = UserSerializer
