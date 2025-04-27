"""
CRUD-операции для работы с записями ежедневника в базе данных.
"""

from sqlalchemy.orm import Session
from src.db.models import DiaryEntry
from src.schemas.schemas import DiaryEntryCreate, DiaryEntryUpdate


def create_entry(db: Session, entry: DiaryEntryCreate) -> DiaryEntry:
    """
    Создание новой записи в базе данных.

    :param db: Сессия БД
    :param entry: Данные новой записи
    :return: Созданная запись
    """
    db_entry = DiaryEntry(**entry.dict())
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)  # <-- ДОБАВЬ ЭТО
    return db_entry


def get_entry(db: Session, entry_id: int) -> DiaryEntry:
    """
    Получение записи по её ID.

    :param db: Сессия БД
    :param entry_id: Идентификатор записи
    :return: Найденная запись или None
    """
    return db.query(DiaryEntry).filter(DiaryEntry.id == entry_id).first()


def get_entries(db: Session, skip: int = 0, limit: int = 100) -> list[DiaryEntry]:
    """
    Получение списка записей.

    :param db: Сессия БД
    :param skip: Количество пропущенных записей
    :param limit: Максимальное количество возвращаемых записей
    :return: Список записей
    """
    return db.query(DiaryEntry).offset(skip).limit(limit).all()


def update_entry(db: Session, entry_id: int, entry_update: DiaryEntryUpdate) -> DiaryEntry:
    """
    Обновление существующей записи.

    :param db: Сессия БД
    :param entry_id: Идентификатор записи
    :param entry_update: Новые данные для записи
    :return: Обновленная запись
    """
    db_entry = get_entry(db, entry_id)
    if db_entry:
        for key, value in entry_update.dict().items():
            setattr(db_entry, key, value)
    return db_entry


def delete_entry(db: Session, entry_id: int) -> DiaryEntry:
    """
    Удаление записи по её ID.

    :param db: Сессия БД
    :param entry_id: Идентификатор записи
    :return: Удаленная запись
    """
    db_entry = get_entry(db, entry_id)
    if db_entry:
        db.delete(db_entry)
    return db_entry
