# 🚀 Клон Твиттера  

Самый сложный и интересный проект, над которым я работал.  

- **Бэкенд**: FastAPI + SQLAlchemy + Alembic  
- **Фронтенд**: Vue.js + Pinia  

## 🛠 Запуск проекта  

### 1️⃣ Подготовка  

Сначала убедитесь, что **Docker** активирован. Если он выключен, включите его командой:  

```sh
sudo systemctl enable docker
```

Также убедитесь, что в `./image_saver` есть само приложение. Если его нет, скачайте репозиторий:  
🔗 [GitHub: image_saver](https://github.com/medin-misha/image_saver.git)  

### 2️⃣ Настройка backend  

Откройте файл `./app/run.sh` и добавьте в него следующий код:  

```sh
#!/bin/sh

export postgres_user=postgres_user
export postgres_password=postgres_password
export postgres_host=<твой_ip_или_ip_postgres>:5432/postgres_db

export image_service_host=http://192.168.5.197:9000/

# Выполнение миграций
alembic upgrade head

# Запуск приложения
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Здесь указаны переменные окружения и все необходимые ссылки для работы сервиса.  

### 3️⃣ Запуск backend  

Теперь можно запустить backend с помощью Docker:  

```sh
docker-compose up --build
```

Подождите, пока завершатся миграции, после чего backend будет доступен на **8000 порту**.  

### 4️⃣ Запуск frontend  

Для работы фронтенда на вашем компьютере должен быть установлен **Node.js**.  

Перейдите в папку `frontend/` и выполните команды:  

```sh
npm install
npm run dev
```

После запуска в терминале появится ссылка, по которой можно открыть приложение и пользоваться. 🎉
