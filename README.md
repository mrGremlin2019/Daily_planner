# Daily Planner

Приложение «Ежедневник» на FastAPI с использованием PostgreSQL и Docker.

## Описание

Daily Planner — это простое RESTful API для создания, чтения, обновления и удаления (CRUD) записей в ежедневнике.  
Каждая запись содержит заголовок, содержание и статус выполнения.

## Функциональность

- Создание новой записи  
- Получение списка записей с параметрами пагинации (`skip`, `limit`)  
- Получение одной записи по ID  
- Обновление записи по ID  
- Удаление записи по ID

## Технологии

- Python 3.10  
- FastAPI  
- SQLAlchemy  
- Pydantic  
- PostgreSQL  
- Docker & Docker Compose  
- Uvicorn

## Настройка переменных окружения
Создайте файл ```.env``` в корне проекта:


```bash
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    POSTGRES_DB=diary_db
    POSTGRES_HOST=db
    POSTGRES_PORT=5432
    MODE=development
```

## Сборка и запуск через Docker Compose

```bash
    docker-compose up --build
```
- fastapi_app будет доступен на http://localhost:8000
- Swagger UI: http://localhost:8000/docs

## Работа без Docker
1. Создать виртуальное окружение и активировать его:

```bash
    python3 -m venv .venv
    source .venv/bin/activate
```
2. Установить зависимости:

``` bash
    pip install -r requirements.txt
```
3. Запустить PostgreSQL локально (или использовать существующий).

4. Заполнить .env (как в примере).

5. Запустить приложение:

```bash
    uvicorn src.main:app --reload
```

Пример схем Pydantic:
```bash
    // DiaryEntryCreate
    {
      "title": "Моя задача",
      "content": "Описание задачи",
      "is_done": false
    }
    
    // DiaryEntryUpdate
    {
      "title": "Новый заголовок",
      "content": "Обновлённое описание",
      "is_done": true
    }
    
    // DiaryEntryOut (ответ)
    {
      "id": 1,
      "title": "Моя задача",
      "content": "Описание задачи",
      "is_done": false
    }
```
