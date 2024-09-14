from fastapi import APIRouter
from app.models import Incidente
from app.database import create_incidente,obtener_incidentes, obtener_incidentes_user


router = APIRouter()

@router.get("/")
async def health():
    return {"status": "ok"}


@router.post("/incidente")
async def crear_incidente(event_data: Incidente ):
    print(event_data)
    incidente = create_incidente(event_data)
    return incidente



@router.get("/incidentes")
async def obtener_todos():
    incidentes = obtener_incidentes()
    return incidentes

@router.get("/incidentes/{user_id}")
async def obtener_incidentes(user_id):
    incidentes = obtener_incidentes_user(user_id)
    return incidentes




