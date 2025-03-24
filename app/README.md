## 📖 Техническая документация  

### `main.py`  
Файл `main.py` содержит код для запуска приложения и подключения роутеров из папки `handlers`.  

Роутеры объявляются в `__init__.py` по принципу `<name>_router`, что позволяет удобно подключать их в `main.py`.  

Дополнительно в `main.py` есть два специальных роутера:  
- **`main()`** — для раздачи фронтенда.  
- **`get_image_view(id)`** — для получения изображения по его `id`.  

---

### 📂 `handlers`  
Папка `handlers` содержит функции-обработчики запросов. В ней также есть папка `utils/`, которая включает вспомогательные функции.  

#### 📌 `utils/` — вспомогательные функции  
Содержит два файла:  
- **`responses.py`** — содержит функции `ok_response` и `error_response`.  
- **`db_actions.py`** — содержит функции для взаимодействия с базой данных.  

#### 🛠 Основные функции  
- **`responses.ok_response(resp)`**  
  Форматирует ответ сервера, добавляя `{ "result": true }`, чтобы он был понятен фронтенду.  
- **`responses.error_response(msg, err_type)`**  
  Возвращает ошибку, которую понимает фронтенд (`msg` — сообщение, `err_type` — статус-код ошибки).  
- **`db_actions.create(model, session, data)`**  
  Создаёт запись в базе данных.  
- **`db_actions.remove(model, session, id)`**  
  Удаляет запись по `id`.  
- **`db_actions.get_by_id(model, session, id)`**  
  Возвращает запись по `id` или `None`.  
- **`db_actions.get_list(model, session)`**  
  Возвращает все записи таблицы.  
- **`get_image.get_image(filename)`**  
  Запрашивает изображение из API, которое хранит изображения.  

---

### ⚙️ `core`  
Папка `core` содержит файлы, необходимые для работы проекта и взаимодействия с базой данных.  

#### 📌 Основные файлы  
- **`config.py`** — файл конфигурации.  
- **`database.py`** — работа с базой данных.  
- **`models/`** — директория с моделями базы данных.  

#### 🛠 Основные классы  
- **`config.Settings`**  
  Конфигурация проекта (поля: `db_url` — URL базы данных, `image_saver_url` — URL сервиса хранения изображений).  
- **`config.settings`**  
  Экземпляр класса `Settings` для удобного импорта.  
- **`database.DBSettings`**  
  Отвечает за взаимодействие с БД (создание движка и сессий).  
- **`database.db_settings`**  
  Экземпляр `DBSettings` для удобного импорта.  
- **`models.base.Base`**  
  Базовый класс моделей БД, включает поле `id` как первичный ключ.  
- **`models.user`, `models.tweet`, `models.image`**  
  Файлы с моделями базы данных.  
- **`models.table_communication`**  
  Файл с промежуточными таблицами для моделей.  

---

## 🧪 Как тестировать?  
1. Запустите тестовую базу данных:  
   ```bash
   docker-compose up --build postgres image_saver
   ```  
2. Примените миграции (если требуеться):  
   ```bash
   alembic upgrade head
   ```  
3. Установите переменные окружения:
  ```bash
	export postgres_user=postgres_user
  export postgres_password=postgres_password
  export postgres_host=192.168.5.197:5432/postgres_db
  export image_service_host=http://192.168.5.197:9000/
  ```
4. Запустите тесты:  
   ```bash
   pytest tests/
   ```  

Готово! 🎯 Теперь всё работает корректно. 🚀  
