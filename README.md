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
## техническая документация
### main.py
В main.py содержиться код для запуска и подключения роутеров которые лежат
в папке handlers.

Роутеры именуются (так как их видно в main.py) в `__init__.py` по принцыпу 
`<name>_router`. 

А так же там лежат роутеры для отдачи фронтенда (main()) и роутер для отдачи изображения по id (get_image_view())

### handlers
В папке handlers лежат функции обработки а так же в отдельной папке вынесены функции для общего использования в рамках обработчиков. 

Папка для функций общего использования называеться utils/ в ней пока что есть 2 файла
- responses.py папка в которой лежат функции ok_response и error_response.
- db_actions.py папка в которой лежат функции для общего взаемодействия со всеми моделей для базы данных

#### Какие функции за что отвечают
- responses.ok_response - Функция которая принимает данные ответа сервера (аргумент resp) и адаптирует данные под понимание фронтенда (по факту просто добавляет к ответу { "result": true })
- response.error_response - Функция которая возвращает ошибку которую понимает фронтенд (принимает аргументы msg - сообщение об ошибке и err_type который по факту являеться status кодом ошибки)
- db_actions.create - Функция которая должна по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД), и данных (data - словарь с данными для модели) создать запись в базе данных.
- db_actions.remove - Функция которая по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД) и id (id записи в БД) удалять запись
- db_actions.get_by_id - Функция которая по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД) и id (id записи в БД) отдаёт запись или None
- db_actions.get_list - Функция которая по модели (model - модель которую нужно создать), сессии (session - асинхронная сессия для связи с БД) возвращает все записи таблицы
- get_image.get_image - Функция которая по filename обращается к специальному API который хранит изображения и отдаёт их, получает изображения которое отдаёт в качестве ответа сервера
### core
В папке core находиться файлы которые необходимы для работы проекта и работы с базой данных
- config.py - файл конфигурации
- database.py - файл работающий с базой данных
- models/ - директория с моделями для базы данных

#### Какие классы за что отвечают?
- config.Settings - класс конфигурации проекта пока что содержит 2 поля db_url - url к базе данных, image_saver_url - url к сервису который будет хранить и выдавать изображения для твитов.
- config.settings - Переменная с экземпляром класса Settings для более удобного импорта
- database.DBSettings - Класс который отвечает за взаемодействие с бд (создание движка (в __init__()) и выдачу сессий (в session()))
- database.db_settings - переменная с экземпляром класса DBSettings для более удобного импорта
- models.base.Base - Класс базовой модели базы данных от которого наследуются другие классы-модели. По умолчанию имеет поле id которое являеться первичным ключом.
- models.user/tweet/image - файлы с моделями базы данных
- models.table_communication - файл с промежуточными таблицами для моделей.

# как тестировать?
Что бы тестировать проект необходимо запустить тестовую бд (docker-compose.postgres_test) после запуска запустить миграции `alembic upgrade head` и тесты `pytest tests/`.
