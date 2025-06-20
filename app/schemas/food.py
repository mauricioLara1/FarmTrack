from pydantic import BaseModel, Field
from decimal import Decimal

#Clase base, contiene los campos comunes que se reutilizan
class FoodBase(BaseModel):
    namefood: str = Field(max_length=25)
    infofood: str = Field(max_length=200)
    amountlb: Decimal = Field(..., max_digits=10, decimal_places=2)

#Clase para crear un nuevo registro
class FoodCreate(FoodBase):
    pass

#Clase para mostrar un registro (incluye ID y campo 'del')
class FoodOut(FoodBase):
    food: int
    del_: bool

    class Config:
        orm_mode = True  # Permite que Pydantic lea datos desde objetos ORM
