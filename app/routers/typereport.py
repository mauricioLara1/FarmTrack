	#typereport SERIAL PRIMARY KEY ,
	#typename varchar(25) UNIQUE NOT NULL,
	#description varchar (200) NOT NULL,
	#del BOOLEAN DEFAULT FALSE
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.typereport import Typereport
from app.schemas.typereport import TypereportCreate, TypereportOut
from app.crud import typereport as crud

router = APIRouter(prefix="/typereports", tags=["Typereports"])

# Obtener todas las carreras
@router.get("/", response_model=list[TypereportOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_typereports(db)

# Crear una nueva carrera
@router.post("/", response_model=TypereportOut)
def create_typereport(Typereport_data: TypereportCreate, db: Session = Depends(get_db)):
    return crud.create_typereport(db=db, typereport_data=Typereport_data)

# Eliminar una carrera (delete real)
@router.delete("/{typereport_id}")
def delete(typereport_id: int, db: Session = Depends(get_db)):
    item = crud.delete_typereport(db, typereport_id)
    if not item:
        raise HTTPException(status_code=404, detail="typereport not found")
    return {"ok": True}

# Soft-delete de una carrera
@router.patch("/soft-delete/{typereport_id}", response_model=TypereportOut)
def soft_delete(typereport_id: int, db: Session = Depends(get_db)):
    item = crud.soft_delete_typereport(db, typereport_id)
    if not item:
        raise HTTPException(status_code=404, detail="typereport not found")
    return item
