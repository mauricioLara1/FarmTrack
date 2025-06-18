from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.Typeworker import Typeworker
from app.schemas.typeWorker import Typeworkercreate, TypeworkerOut
from app.crud import typeworker as crud

router = APIRouter(prefix="/typeworker", tags=["typeworker"])
@router.get("/", response_model=list[TypeworkerOut])
def read_all(db:Session = Depends(get_db)):
    return crud.get_typeworker(db)

@router.post("/", response_model=TypeworkerOut)
def create_typeworker(typeworker_data: Typeworkercreate, db:Session = Depends(get_db)):
    return crud.create_typeworker(db=db, typeworker_data=typeworker_data)


#@router.patch("/soft-delete/{typeworker_id}", response_model=TypeworkerOut)
#def soft_delete(typeworker_id: int, db: Session = Depends(get_db)):
#    item = crud.soft_delete_typeworker(db, typeworker_id)
#    if not item:
#        raise HTTPException(status_code=404, detail="typeworker not found")
#    return item

@router.delete("/{typeworker_id}")
def delete_typeworker(typeworker_id:int, db: Session = Depends(get_db)):
    item = crud.delete_typeworker(db,typeworker_id)
    if not item:
        raise HTTPException(status_code=404, detail="typeworker not found")
    return {"ok": True}

