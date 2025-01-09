from rest_framework.pagination import PageNumberPagination


class HabitsPagination(PageNumberPagination):
    """Пагинация для списка привычек."""

    page_size = 5
