from pydantic import BaseModel, Field

#Clase base, contiene los campos comunes que se reutilizan
class TypereportBase(BaseModel):
    typename: str = Field(max_length=25)
    description: str = Field(max_length=200)

#Clase para crear un nuevo registro
class TypereportCreate(TypereportBase):
    pass

#Clase para mostrar un registro (incluye ID y campo 'del')
class TypereportOut(TypereportBase):
    typereport: int
    del_: bool

    class Config:
        orm_mode = True  # Permite que Pydantic lea datos desde objetos ORM
