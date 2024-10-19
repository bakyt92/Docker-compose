# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь код приложения
COPY . .

# Настраиваем переменные окружения (например, для Django)
ENV PYTHONUNBUFFERED 1

# Запускаем сервер
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
