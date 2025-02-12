## Курсовая работа №5

---
### Проект приложения создания привычек

- Настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.
- Настроены интеграция с Телеграм и отложенная задача через Celery. Реализована работа с 
отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.
Для этого интегрирован сервис с мессенджером Телеграм, который занимается рассылкой уведомлений.
- Реализована пагинация для вывода списка привычек по 5 на страницу.
- Все необходимые эндпоинты реализованы согласно ТЗ (Регистрация, Авторизация, CRUD привычек,
отображение списка привычек пользователя-владельца и отдельно список публичных привычек)
- Настроены все необходимые валидаторы согласно ТЗ
(Исключен одновременный выбор связанной привычки и вознаграждения. 
Время выполнения должно быть не больше 120 секунд.
В связанные привычки могут попадать только привычки с признаком приятной привычки.
У приятной привычки не может быть вознаграждения или связанной привычки.
Нельзя выполнять привычку реже, чем 1 раз в 7 дней.)
- Настроены права доступа согласно ТЗ
(Каждый пользователь имеет доступ только к своим привычкам по механизму CRUD.
Пользователь может видеть список публичных привычек без возможности их как-то редактировать или удалять.)
- Проект покрыли тестами как минимум на 80%.

---
#### Установка и запуск на локальной машине:
клонировать репозиторий [Github](https://github.com/Ascon29/course_work_5_habits)

Для запуска сервера нажмите на кнопку `run`

---

### Запуск проекта на сервере:
 
1. Клонировать репозиторий:
```bash
git clone https://github.com/Ascon29/course_work_5_habits.git
cd course_work_5_habits
```
 
2. Собрать и запустить контейнеры:
```bash
docker-compose up --build -d
```
 
3. Применить миграции:
```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```
 
4. Создать суперпользователя:
```bash
docker-compose exec web python manage.py csu
```
- логин: admin@example.com
- пароль: 123

5. Сервер доступен по адресу:
```
http://158.160.166.235/
```