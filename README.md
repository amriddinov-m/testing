# Задача: Древовидная структура отделов и сотрудники

Описание задачи: Создать веб-приложение на основе Django, которое отображает древовидную структуру отделов и списки сотрудников в организации.

## Требования

- Python 3.x
- Django
- Django MPTT
- PostgreSql

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/amriddinov-m/traffic_light.git
   
2. Создайте и активируйте виртуальное окружение:
  python -m venv venv
  source venv/bin/activate  # для Linux/macOS

3. Установите зависимости:
  pip install -r requirements.txt

4. Создайте PosgtesSql базу и создайте файл .env и укажите данные(DB_USER, DB_NAME, DB_PASS)

5. Примените миграции:
  python manage.py migrate

6. Генерация данных:
  python manage.py generic_data

7. Запустите сервер:
  python manage.py runserver
  
8. Откройте приложение в вашем веб-браузере по адресу http://localhost:8000/
