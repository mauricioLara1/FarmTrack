from sqlalchemy.orm import Session
from app.models.shedState import Shedstate
from app.schemas.shedstate import Shedstatebase, Shedstatecreate

def get_shedstates(db:Session):
    return db.query(Shedstate).filter(Shedstate.del_ == False).all()

def create_shedstate(db:Session, shedstate_data: Shedstatecreate):
    db_item = Shedstate(**shedstate_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def soft_delete_shedstate(db: Session, shedstate_id:int):
    db_item = db.query(Shedstate).filter(Shedstate.shedstate == shedstate_id).first()
    if db_item:
        db_item.del_=True
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_shedstate(db:Session, shedstate_id: int):
    db_item = db.query(Shedstate).filter(Shedstate.shedstate == shedstate_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item