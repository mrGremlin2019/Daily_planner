"""
Модели базы данных для приложения ежедневника.
"""

from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DiaryEntry(Base):
    """
    Модель записи ежедневника.
    """
    __tablename__ = "diary_entries"

    id = Column(Integer, primary_key=True, index=True, doc="Идентификатор записи")
    title = Column(String(100), nullable=False, doc="Заголовок записи")
    content = Column(Text, nullable=False, doc="Содержимое записи")
    is_done = Column(Boolean, default=False, doc="Статус выполнения записи")

