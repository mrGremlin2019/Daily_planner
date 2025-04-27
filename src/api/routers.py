from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import DiaryEntryCreate, DiaryEntryUpdate, DiaryEntryOut
from src.db import crud
from src.db.config_db import get_db

router = APIRouter(
    prefix="/entries",
    tags=["Diary Entries"]
)


@router.post("/", response_model=DiaryEntryOut)
def create_diary_entry(entry: DiaryEntryCreate, db: Session = Depends(get_db)):
    """
    Создание новой записи.
    """
    db_entry = crud.create_entry(db=db, entry=entry)
    return db_entry


@router.get("/", response_model=list[DiaryEntryOut])
def read_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Получение списка всех записей.
    """
    return crud.get_entries(db=db, skip=skip, limit=limit)


@router.get("/{entry_id}", response_model=DiaryEntryOut)
def read_entry(entry_id: int, db: Session = Depends(get_db)):
    """
    Получение одной записи по ID.
    """
    db_entry = crud.get_entry(db=db, entry_id=entry_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry


@router.put("/{entry_id}", response_model=DiaryEntryOut)
def update_entry(entry_id: int, entry: DiaryEntryUpdate, db: Session = Depends(get_db)):
    """
    Обновление записи по ID.
    """
    db_entry = crud.update_entry(db=db, entry_id=entry_id, entry_update=entry)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry


@router.delete("/{entry_id}", response_model=DiaryEntryOut)
def delete_entry(entry_id: int, db: Session = Depends(get_db)):
    """
    Удаление записи по ID.
    """
    db_entry = crud.delete_entry(db=db, entry_id=entry_id)
    if not db_entry:
        raise HTTPException(status_code=404, detail="Entry not found")
    return db_entry
