from sqlalchemy.orm import Session
from app.models.Typeworker import Typeworker
from app.schemas.typeWorker import Typeworkerbase,Typeworkercreate

def get_typeworker(db:Session):
    return db.query(Typeworker).all()

def create_typeworker(db:Session, typeworker_data: Typeworkercreate):
    db_item = Typeworker(**typeworker_data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#agregar el del a la tabla
#def soft_delete_typeworker(db:Session, typeworker_id: int):
#    db_item = db.query(Typeworker).filter(Typeworker.typeworker == typeworker_id). first()
#    if db_item:
#        db_item.del_=True
#        db.commit()
#        db.refresh(db_item)
#    return db_item

def delete_typeworler(db:Session, typeworker_id:int):
    db_item = db.query(Typeworker).filter(typeworker_id == Typeworker).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

