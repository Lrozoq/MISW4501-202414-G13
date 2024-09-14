from sqlmodel import Session, create_engine, SQLModel
from app import config
from app.models import Incidente
from google.cloud import pubsub_v1

# URL para la base de datos primaria
SQLALCHEMY_DATABASE_URL_PRIMARY = f"mysql+mysqlconnector://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
print(SQLALCHEMY_DATABASE_URL_PRIMARY)

# URL para la base de datos réplica
SQLALCHEMY_DATABASE_URL_REPLICA = f"mysql+mysqlconnector://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST_REPLICA}:{config.DB_PORT_REPLICA}/{config.DB_NAME_REPLICA}"

# Crear motores para las dos bases de datos
engine_primary = create_engine(SQLALCHEMY_DATABASE_URL_PRIMARY)
engine_replica = create_engine(SQLALCHEMY_DATABASE_URL_REPLICA)

# Inica Pub/Sub Publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(config.PROJECT_ID, config.TOPIC_ID)

# Crear las tablas en la base de datos primaria
SQLModel.metadata.create_all(engine_primary)

def create_session(primary: bool = True):
    """Crea una sesión, usa la primaria si primary=True, de lo contrario usa la réplica."""
    if primary:
        session = Session(engine_primary)
    else:
        session = Session(engine_replica)
    return session

def create_incidente(incidente: Incidente):
    """Crea un incidente en la base de datos primaria."""
    session = create_session(primary=True)  # Siempre en la primaria
    session.add(incidente)
    session.commit()
    session.refresh(incidente)
    session.close()
    return incidente

def obtener_incidentes():
    """Obtiene todos los incidentes desde la base de datos réplica."""
    session = create_session(primary=False)  # Para Consultas desde la réplica cambiarle el valor a false
    incidentes = session.query(Incidente).all()
    session.close()
    return incidentes


def obtener_incidentes_user(user_id: int):
    """Obtiene todos los incidentes de un usuario desde la réplica."""
    session = create_session(primary=False)# Para Consultas desde la réplica cambiarle el valor a false
    incidentes = session.query(Incidente).filter(Incidente.user_id == user_id).all()
    session.close()
    return incidentes
