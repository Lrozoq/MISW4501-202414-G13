import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv("DB_USER_PRIMARY","prueba")
DB_PASSWORD = os.getenv("DB_PASSWORD_PRIMARY","prueba")
DB_HOST = os.getenv("DB_HOST_PRIMARY","localhost")
DB_NAME = os.getenv("DB_NAME_PRIMARY","prueba")
DB_PORT = os.getenv("DB_PORT_PRIMARY","5432")

DB_USER_REPLICA = os.getenv("DB_USER_REPLICA","prueba")
DB_PASSWORD_REPLICA = os.getenv("DB_PASSWORD_REPLICA","prueba")
DB_HOST_REPLICA = os.getenv("DB_HOST_REPLICA","localhost")
DB_NAME_REPLICA = os.getenv("DB_NAME_REPLICA","prueba")
DB_PORT_REPLICA = os.getenv("DB_PORT_REPLICA","5432")

PROJECT_ID = os.getenv("GCP_PROJECT_ID", "abcall-435301")
TOPIC_ID = os.getenv("GCP_TOPIC_ID", "incidents-db-sync")
ENV = os.getenv("ENV")

if ENV:
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
REDIS_PORT = os.getenv('DOCKER_REDIS_PORT', 6379)
REDIS_SERVICE_NAME = os.getenv('DOCKER_REDIS_SERVICE_NAME')

DB_SOCKET_PATH_PRIMARY = os.getenv("DB_SOCKET_PATH_PRIMARY", "")
DB_SOCKET_PATH_REPLICA = os.getenv("DB_SOCKET_PATH_REPLICA", "")