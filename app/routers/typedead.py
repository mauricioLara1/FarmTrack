
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.typedead import Typedead
from app.schemas.typedead import Typedeadcreate, TypedeadOut
from app.crud import typedead as crud

router = APIRouter(prefix="/typedead", tags=["typedead"])

# Obtener todas las carreras
@router.get("/", response_model=list[TypedeadOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_typedeads(db)

# Crear una nueva carrera
@router.post("/", response_model=TypedeadOut)
def create_typedead(typedead_data: Typedeadcreate, db: Session = Depends(get_db)):
    return crud.create_typedead(db=db, typedead_data=typedead_data)

# Eliminar una carrera (delete real)
@router.delete("/{typedead_id}")
def delete(typedead_id: int, db: Session = Depends(get_db)):
    item = crud.delete_typedead(db, typedead_id)
    if not item:
        raise HTTPException(status_code=404, detail="typedead not found")
    return {"ok": True}

# Soft-delete de una carrera
@router.patch("/soft-delete/{typedead_id}", response_model=TypedeadOut)
def soft_delete(typedead_id: int, db: Session = Depends(get_db)):
    item = crud.soft_delete_typedead(db, typedead_id)
    if not item:
        raise HTTPException(status_code=404, detail="typedead not found")
    return item
