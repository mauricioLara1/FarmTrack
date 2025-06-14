#estas  importaciones son porque importamos un modelo de base de datos y no estructuras python
#string boolean integer: son los tipos de las db para poder trasfromarlos
#column: son columna de una tabla sql
from sqlalchemy import Column, Integer, String, Boolean
#el base es el modelo que se usa, dando que la base es nuestro molde
from app.db.config import Base

#se crea una clase por tabla en la db
class BatchState(Base):
    #con esto sabemos que cuando llamemos el modelo, que tabla debe buscar en la base de datos
    __tablename__ = "batchstate"

    #aqui asignamos a la clase de esta manera
    #varName = Column("columnName",vartype,pk o fk, entre todos los demas extras de la columna )
    batchstate = Column(Integer, primary_key=True, index=True)
    batchname = Column(String(25), nullable=False)
    #el del esta como del_ porque del es una palabra reservada en Python 
    del_ = Column("del",Boolean, default=False)
