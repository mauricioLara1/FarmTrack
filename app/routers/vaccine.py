from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.vaccine import Vaccine
from app.schemas.vaccine import Vaccinecreate, VaccineOut
from app.crud import vaccine as crud

router = APIRouter(prefix="/vaccine", tags=["vaccine"])
@router.get("/", response_model=list[VaccineOut])
def read_all(db:Session = Depends(get_db)):
    return crud.get_vaccine(db)

@router.post("/", response_model=VaccineOut)
def create_vaccine(vaccine_data: Vaccinecreate, db:Session = Depends(get_db)):
    return crud.create_vaccine(db=db, vaccine_data=vaccine_data)


#@router.patch("/soft-delete/{vaccine_id}", response_model=VaccineOut)
#def soft_delete(vaccine_id: int, db: Session = Depends(get_db)):
#    item = crud.soft_delete_vaccine(db, vaccine_id)
#    if not item:
#        raise HTTPException(status_code=404, detail="vaccine not found")
#    return item

@router.delete("/{vaccine_id}")
def delete_vaccine(vaccine_id:int, db: Session = Depends(get_db)):
    item = crud.delete_vaccine(db,vaccine_id)
    if not item:
        raise HTTPException(status_code=404, detail="vaccine not found")
    return {"ok": True}

