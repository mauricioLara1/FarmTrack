from fastapi import FastAPI
from app.routers import batchstate

app = FastAPI()

app.include_router(batchstate.router, prefix="/batchstate", tags=["batchstate"])

# Ruta raíz opcional
@app.get("/")
def root():
    return {"message": "FarmTrack API en funcionamiento "}

# Incluir todos los routers
app.include_router(batchstate.router)