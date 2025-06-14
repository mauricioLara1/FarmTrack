#Crud: Create - Read - Update - Delete
#este archivo y carpeta tiene la tarea de redactar las operaciones sql 

#obj que hace de sesion sql para las consultas:
from sqlalchemy.orm import Session
#modelo de tabla sql que usamos:
from app.models.batchstate import BatchState
#esquema que valida los datos que llega del modelo:
from app.schemas.batchstate import BatchStateCreate

#crear la estructura de un nuevo registro en la base de datos
def create_batchstate(db: Session, batchstate: BatchStateCreate):
    #BatchState(**...) : se usa el diccionario para crear la instancia del modelo
    #batchstate.dict() : creamos un diccionario con el obj
    db_item = BatchState(**batchstate.dict())
    #prepara los datos en la seccion actual sin aun guardarlos en la db
    db.add(db_item)
    #se da confirmar, guardando los en la db
    db.commit()
    #recargamos la base de datos que tenemos descargada
    db.refresh(db_item)
    #retornamos lo que se creo
    return db_item

#obtener todas las filas donde del sea falso (que no se han borrado)
def get_batchstates(db: Session):
    #db.query(BatchState): es una consulta a la tabla
    #.filter(BatchState.del_ == False): es una condicional para que solo se quede los false}
    #.all():es el obtener todo lo que quedo
    return db.query(BatchState).filter(BatchState.del_ == False).all()

#!!!permanente!!! eliminar el dato que tenga como pk el dato que usamos en el batchstate_id 
def delete_batchstate(db: Session, batchstate_id: int):
    #se hace una consulta en la tabla atchstate, donde le aplicamos el filtro para obtener solo el batchstate_id
    db_item = db.query(BatchState).filter(BatchState.batchstate == batchstate_id).first()
    #no entiendo para que es el if
    if db_item:
        #se hace uso del delete dentro de la secion para borrarlo
        db.delete(db_item)
        #se confirma el delete
        db.commit()
    return db_item

#suave: se actualiza la columna del para que entonces el dato quede como borrador el dato que tenga como pk el dato que usamos en el batchstate_id
def soft_delete_batchstate(db: Session, batchstate_id: int):
    #esta es una consulta con el filtro del batchstate_id
    db_item = db.query(BatchState).filter(BatchState.batchstate == batchstate_id).first()
    if db_item:
        #el objeto que obtivos el db_item le cambiamos el dato .del para que sea verdad el borrado
        db_item.del_ = True
        #se confirma el cambio para la db y recarlagmos informacion
        db.commit()
        db.refresh(db_item)
    return db_item
