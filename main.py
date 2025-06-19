from fastapi import FastAPI
from app.routers import batchstate, race, shedState,typeworker,vaccine,typedead

app = FastAPI()

app.include_router(batchstate.router, prefix="/batchstate", tags=["batchstate"])
app.include_router(race.router) 
app.include_router(shedState.router)
app.include_router(typeworker.router)
app.include_router(vaccine.router)
app.include_router(typedead.router)

# Ruta raíz opcional
@app.get("/")
def root():
    return {"message": "FarmTrack API en funcionamiento "}

# Incluir todos los routers
app.include_router(batchstate.router)