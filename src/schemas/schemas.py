"""
Схемы валидации данных для работы с API ежедневника.
"""

from pydantic import BaseModel

class DiaryEntryBase(BaseModel):
    """
    Базовая схема записи ежедневника.
    """
    title: str
    content: str

class DiaryEntryCreate(DiaryEntryBase):
    """
    Схема для создания новой записи.
    """
    pass

class DiaryEntryUpdate(DiaryEntryBase):
    """
    Схема для обновления записи.
    """
    is_done: bool

class DiaryEntryOut(DiaryEntryBase):
    """
    Схема для отображения записи в ответах API.
    """
    id: int
    is_done: bool

    class Config:
        orm_mode = True