FROM python:3.12-slim

WORKDIR /app

COPY main.py .

EXPOSE 8080

CMD ["python3", "main.py"]# Використовуємо офіційний образ Python
FROM python:3.12-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо файл проекту
COPY main.py .

# Відкриваємо порт 8080
EXPOSE 8080

# Запускаємо сервер
CMD ["python3", "main.py"]
