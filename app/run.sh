#!/bin/sh

export postgres_user=postgres_user
export postgres_password=postgres_password
export postgres_host=postgres:5432/postgres_db

export image_service_host=http://192.168.2.6:9000/
# Выполнение миграций
alembic upgrade head

# Запуск приложения
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --reload
