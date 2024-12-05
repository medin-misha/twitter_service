#!/bin/sh
set -e

# Выполнение миграций
alembic upgrade head

# Запуск приложения
exec gunicorn main:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
