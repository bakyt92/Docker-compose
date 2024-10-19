# Простое приложение

## Работа с проектом
Для работы с проектом использовать команду
```
docker-compose up
```

## Первый запуск
- Создается Dockerfile, docker-compose.yml, requirements.txt
- Запускаем
    ```
    docker-compose up --build
    ```
- В терминале выполнияется команда для создания проекта
    - Создаем проект
        ```
        docker-compose run web django-admin startproject myproject .
        ```
    - Создаем приложение
        ```
        docker-compose run web python manage.py startapp myapp
        ```
- настраиваем
    - В myproject/settings.py добавляется приложение
        ```
        INSTALLED_APPS = [
            ...
            'myapp',
        ]
    - В myapp/views.py создается простое представление:
        ```
        from django.http import HttpResponse
        def index(request):
            return HttpResponse("Привет из Django!")
    - добавляется URL-адрес в myproject/urls.py:
        ```
        from myapp import views
        urlpatterns = [
            path('', views.index, name='index'),
        ]
- подключаем БД
    - Настраивается myproject/settings.py
        ```
        import os
        from decouple import config

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': config('POSTGRES_DB', default='mydatabase'),
                'USER': config('POSTGRES_USER', default='myuser'),
                'PASSWORD': config('POSTGRES_PASSWORD', default='mypassword'),
                'HOST': 'db',  # Имя сервиса из docker-compose
                'PORT': '5432',
            }
        }
    - Создается файл .env
        ```
        POSTGRES_DB=mydatabase
        POSTGRES_USER=myuser
        POSTGRES_PASSWORD=mypassword
    - Создаются миграции
        ```
        docker-compose run web python manage.py makemigrations
        docker-compose run web python manage.py migrate
    - Обновляется myapp/views.py
        ```
        from django.http import HttpResponse
        from django.db import connection
        def index(request):
            with connection.cursor() as cursor:
                cursor.execute("SELECT version();")
                db_version = cursor.fetchone()
            return HttpResponse(f"Привет из Django!, и база данных: {db_version[0]}")
- Запускаем http://localhost:8000
    ```
    docker-compose up
    ```