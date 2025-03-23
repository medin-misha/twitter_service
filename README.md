\## не жалкий клон твиттера
Корпоративный клон твиттера с отсутствующей регистрацией. Вот как то так.
## как запустить? 
Запуск производиться невероятно просто. 
Достаточно только активировать Docker если оно не активированно: 
```commandline
sudo systemctl enable docker
```

Далее убедитесь что в ./image_saver есть само приложение. Если его нет то скачайте его репозиторий: https://github.com/medin-misha/image_saver.git

Теперь заходем в ./app/run.sh и пишем сюда следуйщий код:
```sh
#!/bin/sh

export postgres_user=postgres_user
export postgres_password=postgres_password
export postgres_host=<твой ip или ip postrgers>:5432/postgres_db

export image_service_host=http://192.168.5.197:9000/
# Выполнение миграций
alembic upgrade head

# Запуск приложения
uvicorn main:app --reload --host 0.0.0.0 --port 8000 --reload
```
Команда для заупска всего этого дела:
```commandline
docker-compose up --build
```
И нужно подождать пока проведуться миграции и после запуска можно будет заходить на 8000 порт и смотреть.

Что бы создать user-a заходите в /docs
## как зопустить в не docker
всё очень тривеально. Заходим в /app копируем зависимости 
```commandline
pip install -r requirements.txt
```
запускаем (предварительно незабыв убедиться что в .env файле есть ссылка на базу данных postgres)
db_url в .env обязательное поле.
по умолчанию стоит "postgresql+asyncpg://postgres_user:postgres_password@192.168.5.194:5432/postgres_db"

так вот после запуска postgres(способ на ваш выбор) запускаем из /app миграции
```commandline
alembic upgrade head
```
и запускаем uvicorn
```commandline
uvicorn main:app --reload
```
готово
