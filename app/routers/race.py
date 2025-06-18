from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.race import Race
from app.schemas.race import RaceCreate, RaceOut
from app.crud import race as crud

router = APIRouter(prefix="/races", tags=["Races"])

# Obtener todas las carreras
@router.get("/", response_model=list[RaceOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_races(db)

# Crear una nueva carrera
@router.post("/", response_model=RaceOut)
def create_race(race_data: RaceCreate, db: Session = Depends(get_db)):
    return crud.create_race(db=db, race_data=race_data)

# Eliminar una carrera (delete real)
@router.delete("/{race_id}")
def delete(race_id: int, db: Session = Depends(get_db)):
    item = crud.delete_race(db, race_id)
    if not item:
        raise HTTPException(status_code=404, detail="race not found")
    return {"ok": True}

# Soft-delete de una carrera
@router.patch("/soft-delete/{race_id}", response_model=RaceOut)
def soft_delete(race_id: int, db: Session = Depends(get_db)):
    item = crud.soft_delete_race(db, race_id)
    if not item:
        raise HTTPException(status_code=404, detail="race not found")
    return item
