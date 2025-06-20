from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.config import get_db
from app.models.food import Food
from app.schemas.food import FoodCreate, FoodOut
from app.crud import food as crud

router = APIRouter(prefix="/foods", tags=["Foods"])

# Obtener todas las carreras
@router.get("/", response_model=list[FoodOut])
def read_all(db: Session = Depends(get_db)):
    return crud.get_foods(db)

# Crear una nueva carrera
@router.post("/", response_model=FoodOut)
def create_food(Food_data: FoodCreate, db: Session = Depends(get_db)):
    return crud.create_food(db=db, food_data=Food_data)

# Eliminar una carrera (delete real)
@router.delete("/{food_id}")
def delete(food_id: int, db: Session = Depends(get_db)):
    item = crud.delete_food(db, food_id)
    if not item:
        raise HTTPException(status_code=404, detail="food not found")
    return {"ok": True}

# Soft-delete de una carrera
@router.patch("/soft-delete/{food_id}", response_model=FoodOut)
def soft_delete(food_id: int, db: Session = Depends(get_db)):
    item = crud.soft_delete_food(db, food_id)
    if not item:
        raise HTTPException(status_code=404, detail="food not found")
    return item
