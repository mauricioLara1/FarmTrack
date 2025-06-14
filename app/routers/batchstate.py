#fast api es la encargada de dar forma a la api
#apirouter: organiaza rutas en grupos
#depends: inycta dependencias como la db
#httprxception: identifica las exceptcciones http y las imprime
from fastapi import APIRouter, Depends, HTTPException
#esto es solo la sesion a la db
from sqlalchemy.orm import Session
#aqui traemos a la ruta la configuracion de la conexion a la db y la conexion a la db
from app.db.config import get_db
#este es un acceso al modelo que da la forma a como se muestra la informacion
from app.models.batchstate import BatchState
#este es un acceso al modelo que la api espera al crear o devolver un batchstate
from app.schemas.batchstate import BatchStateCreate, BatchStateOut
#traemos el crud que es donde estan las opraciones sql
from app.crud import batchstate as crud

router = APIRouter(prefix="/batchstates", tags=["BatchStates"])

@router.post("/", response_model=BatchStateOut)
def create(batch: BatchStateCreate, db: Session = Depends(get_db)):
    return crud.create_batchstate(db, batch)

@router.get("/", response_model=list[BatchStateOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_batchstates(db)

@router.delete("/{batchstate_id}")
def delete(batchstate_id: int, db: Session = Depends(get_db)):
    item = crud.delete_batchstate(db, batchstate_id)
    if not item:
        raise HTTPException(status_code=404, detail="BatchState not found")
    return {"ok": True}

@router.patch("/soft-delete/{batchstate_id}", response_model=BatchStateOut)
def soft_delete(batchstate_id: int, db: Session = Depends(get_db)):
    item = crud.soft_delete_batchstate(db, batchstate_id)
    if not item:
        raise HTTPException(status_code=404, detail="BatchState not found")
    return item
