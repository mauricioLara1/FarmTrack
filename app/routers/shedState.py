from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.shedState import Shedstate
from app.schemas.shedstate import Shedstatecreate, ShedstateOut
from app.crud import shedState as crud

router = APIRouter(prefix="/shedState", tags=["shedState"])

@router.get("/", response_model=list[ShedstateOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_shedstates(db)

@router.post("/", response_model=ShedstateOut)
def create_shedstate(shedstate_data: Shedstatecreate, db:Session = Depends(get_db)):
    return crud.create_shedstate(db=db, shedstate_data=shedstate_data)

@router.patch("/soft-delete/{shedstate_id}", response_model=ShedstateOut)
def soft_delete(shedstate_id: int, db: Session = Depends(get_db)):
    item = crud.soft_delete_shedstate(db, shedstate_id)
    if not item:
        raise HTTPException(status_code=404, detail="shedstate not found")
    return item

@router.delete("/{shedstate_id}")
def delete_shedstate(shedstate_id:int, db: Session = Depends(get_db)):
    item = crud.delete_shedstate(db,shedstate_id)
    if not item:
        raise HTTPException(status_code=404, detail="shedstate not found")
    return {"ok": True}

