from pydantic import BaseModel, Field

#Clase base, contiene los campos comunes que se reutilizan
class RaceBase(BaseModel):
    racename: str = Field(max_length=25)
    description: str = Field(max_length=200)
    minweigh: float
    maxweigh: float

#Clase para crear un nuevo registro
class RaceCreate(RaceBase):
    pass

#Clase para mostrar un registro (incluye ID y campo 'del')
class RaceOut(RaceBase):
    race: int
    del_: bool

    class Config:
        orm_mode = True  # Permite que Pydantic lea datos desde objetos ORM
