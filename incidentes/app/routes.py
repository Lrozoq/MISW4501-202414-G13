from fastapi import APIRouter
from app.models import Incidente
from app.database import create_incidente,obtener_incidentes, obtener_incidentes_cache, obtener_incidentes_user, create_incidente_cache


router = APIRouter()

@router.get("/")
async def health():
    return {"status": "ok"}


@router.post("/incidente")
async def crear_incidente(event_data: Incidente ):
    event_data.id = None
    incidente = create_incidente(event_data)
    return incidente


@router.post("/incidente_cache")
async def crear_incidente_cache(event_data: Incidente ):
    event_data.id = None
    incidente = create_incidente_cache(event_data)
    return incidente


@router.get("/incidentes")
async def obtener_todos():
    incidentes = obtener_incidentes()
    return incidentes


@router.get("/incidentes_cache")
async def obtener_todos_cache():
    incidentes =  obtener_incidentes_cache()
    return incidentes

@router.get("/incidentes/{user_id}")
async def obtener_incidentes_por_user(user_id):
    incidentes = obtener_incidentes_user(user_id)
    return incidentes

