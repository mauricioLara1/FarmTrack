from pydantic import BaseModel, Field

class Vaccinebase(BaseModel):
    vaccinename: str = Field(max_length=25)
    vaccinedescription: str = Field(max_length=200)

class Vaccinecreate(Vaccinebase):
    pass

class VaccineOut(Vaccinebase):
    vaccine:int

    class Config:
        orm_mode = True

