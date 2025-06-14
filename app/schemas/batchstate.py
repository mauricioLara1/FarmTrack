#pydantic: lireria para validar datos, crear estructuras
#base model es una base de esquema de validacion de datos
from pydantic import BaseModel

#estas son clases de instrucciones sql, que no usamos desde el model porque usamos el models.py para guardar cosas en la bd
#tambien permite tener datos limpios, validarlos y que esten correctos

#esta es una clase que guarda los campos comunes que tengas. usando el model para acomdarlos como los vemos en postman
#en otras palabras pydantic es como un formulario para recibbir y mostrar datos estructurados 
class BatchStateBase(BaseModel):
    batchname: str

class BatchStateCreate(BatchStateBase):
    pass

class BatchStateOut(BatchStateBase):
    batchstate: int
    del_: bool

    class Config:
        orm_mode = True
