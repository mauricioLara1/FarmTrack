from sqlalchemy.orm import Session
from app.models.vaccine import Vaccine
from app.schemas.vaccine import Vaccinebase,Vaccinecreate

def get_vaccine(db:Session):
    return db.query(Vaccine).all()


def create_vaccine(db:Session, vaccine_data: Vaccinecreate):
    db_item = Vaccine(**vaccine_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#agregar el del a la tabla
#def soft_delete_vaccine(db:Session, vaccine_id: int):
#    db_item = db.query(Vaccine).filter(Vaccine.vaccine == vaccine_id). first()
#    if db_item:
#        db_item.del_=True
#        db.commit()
#        db.refresh(db_item)
#    return db_item

def delete_vaccine(db:Session, vaccine_id:int):
    db_item = db.query(Vaccine).filter(vaccine_id == Vaccine.vaccine).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

