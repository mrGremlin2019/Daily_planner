"""
Точка входа в приложение FastAPI
"""

from fastapi import FastAPI
from src.db.config_db import engine
from src.db.models import Base
from src.api.routers import router as diary_router
import logging

app = FastAPI(title="Daily Planner",
              description="""Ежидневник\n """
                          """\nТаблица `diary_entries` содержит следующие поля:\n"""
                          """- **id**: Идентификатор записи (целое число, уникальное для каждой записи).\n"""
                          """ - **title**: Заголовок записи (строка, максимальная длина 100 символов).\n"""
                          """ - **content**: Содержимое записи (текст, неограниченная длина).\n"""
                          """ - **is_done**: Статус выполнения записи (булевое значение: `True` - выполнена, `False` - не выполнена)."""
              )

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

def init_db():
    """Инициализация таблиц БД"""
    Base.metadata.create_all(bind=engine)

@app.on_event("startup")
async def startup_event():
    """Запуск приложения"""
    init_db()
    app.include_router(diary_router)
    logger.info("Application started")
