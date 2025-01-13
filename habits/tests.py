from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@mail.ru", tg_chat_id="test id")
        self.habit = Habit.objects.create(
            owner=self.user, place="test place", time="13:00:00", action="test action", is_public=False
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тест просмотра одной привычки."""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("owner"), self.habit.owner.id)

    def test_habit_create(self):
        """Тест создания привычки."""
        url = reverse("habits:habit-create")
        data = {
            "place": "test place 2",
            "time": "14:00:00",
            "action": "test action 2",
            "time_to_complete": 60,
            "periodicity": 2,
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_update(self):
        """Тест обновления привычки."""
        url = reverse("habits:habit-update", args=(self.habit.pk,))
        data = {"place": "test place 3", "time_to_complete": 60, "periodicity": 2}
        response = self.client.patch(url, data)
        new_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(new_data.get("place"), data.get("place"))

    def test_habit_delete(self):
        """Тест удаления привычки."""
        url = reverse("habits:habit-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_user_list(self):
        """Тест просмотра списка привычек пользователя."""
        url = reverse("habits:habits-user-list")
        response = self.client.get(url)
        data = response.json().get("results")[0]
        result = {
            "id": self.habit.id,
            "place": self.habit.place,
            "time": self.habit.time,
            "action": self.habit.action,
            "is_pleasant": self.habit.is_pleasant,
            "reward": self.habit.reward,
            "periodicity": self.habit.periodicity,
            "time_to_complete": self.habit.time_to_complete,
            "is_public": self.habit.is_public,
            "owner": self.habit.owner.id,
            "associated_habit": self.habit.associated_habit,
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_habit_public_list(self):
        """Тест просмотра списка публичных привычек."""
        url = reverse("habits:habits-public-list")
        response = self.client.get(url)
        data = response.json()
        result = {"count": 0, "next": None, "previous": None, "results": []}

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_wrong_time_to_complete(self):
        """Тест создания привычки при неправильном выборе времени выполнения"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "test place 2",
            "time": "14:00:00",
            "action": "test action 2",
            "time_to_complete": 140,
            "periodicity": 2,
        }
        response = self.client.post(url, wrong_habit_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json().get("non_field_errors"), ["Время выполнения не может превышать 120 секунд"])

    def test_wrong_periodicity(self):
        """Тест создания привычки при неправильном выборе периодичности выполнения"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "test place 2",
            "time": "14:00:00",
            "action": "test action 2",
            "time_to_complete": 120,
            "periodicity": 8,
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"), ["Привычка должна выполняться не реже чем раз в 7 дней"]
        )

    def test_wrong_create_reward_associated_habit(self):
        """Тест создания привычки при одновременном выборе связанной привычки и вознаграждении"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "test place 2",
            "time": "14:00:00",
            "action": "test action 2",
            "time_to_complete": 120,
            "periodicity": 1,
            "associated_habit": self.habit.id,
            "reward": "test reward 2",
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Нельзя выбирать связанную привычку и вознаграждение одновременно"],
        )

    def test_wrong_create_associated_habit_not_pleasant(self):
        """Тест создания связанной привычки без признака приятной привычки"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "test place 2",
            "time": "14:00:00",
            "action": "test action 2",
            "time_to_complete": 120,
            "periodicity": 1,
            "associated_habit": self.habit.id,
            "is_pleasant": False,
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"), ["Связанная привычка должна быть с признаком приятной привычки"]
        )

    def test_wrong_create_is_pleasant_with_reward_or_associated_habit(self):
        """Тест создания привычки с признаком приятной, у которой указали вознаграждение или связанную привычку"""
        url = reverse("habits:habit-create")
        wrong_habit_data = {
            "place": "test place 2",
            "is_pleasant": True,
            "time": "14:00:00",
            "action": "test action 2",
            "time_to_complete": 120,
            "periodicity": 1,
            "associated_habit": "",
            "reward": "test reward 2",
        }
        response = self.client.post(url, wrong_habit_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["У приятной привычки не может быть вознаграждения или связанной привычки"],
        )
