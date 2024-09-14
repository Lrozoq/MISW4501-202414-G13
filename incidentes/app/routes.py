import json
from fastapi import APIRouter, HTTPException
from app.models import Incidente
from app.database import create_incidente,obtener_incidentes, obtener_incidentes_cache, create_incidente_cache, obtener_incidentes_user, publisher, topic_path


router = APIRouter()

@router.get("/")
async def health():
    return {"status": "ok"}


@router.post("/incidente")
async def crear_incidente(event_data: Incidente):
    print(event_data)
    incidente = create_incidente(event_data)
    message_data = event_data.dict()
    try:
        future = publisher.publish(topic_path, json.dumps(message_data).encode("utf-8"))
        message_id = future.result()
        return {"incidente": incidente, "message_id": message_id}
    
    except Exception as e:
        print(f"Failed to publish message to Pub/Sub: {e}")
        
        raise HTTPException(status_code=500, detail="Incident created, but failed to publish message to Pub/Sub.")
    

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
async def obtener_incidentes(user_id: int):
    incidentes = obtener_incidentes_user(user_id)
    return incidentes
