# Используем официальный образ Nginx
FROM nginx:alpine

# Устанавливаем конфигурацию Nginx (если необходимо)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Копируем статические файлы во фронтенд
COPY ./static /usr/share/nginx/html/static