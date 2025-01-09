from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitUserListAPIView, HabitPublicListAPIView, HabitRetrieveAPIView, HabitCreateAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habits/', HabitPublicListAPIView.as_view(), name='habits-public-list'),
    path('habits_user/', HabitUserListAPIView.as_view(), name='habits-user-list'),
    path('habits/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-detail'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
]
