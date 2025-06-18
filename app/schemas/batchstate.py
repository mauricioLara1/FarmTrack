#pydantic: lireria para validar datos, crear estructuras
#base model es una base de esquema de validacion de datos
from pydantic import BaseModel, Field

#estas son clases de instrucciones sql, que no usamos desde el model porque usamos el models.py para guardar cosas en la bd
#tambien permite tener datos limpios, validarlos y que esten correctos

#esta es una clase que guarda los campos comunes que tengas. usando el model para acomdarlos como los vemos en postman
#en otras palabras pydantic es como un formulario para recibbir y mostrar datos estructurados 

#base es los campos los cuales recibe o mueve en la tabla, en este caso la pk se asigna automaticamente y el del es automaticamente asignado quedando solo el nombre
class BatchStateBase(BaseModel):
    batchname: str = Field(max_length=25)

#el create recibe al base, como los datos minimos que ocupa para crear un obj
class BatchStateCreate(BatchStateBase):
    pass

#los datos que se van a mostrar, o el get
class BatchStateOut(BatchStateBase):
    batchstate: int
    del_: bool

    class Config:
        orm_mode = True
