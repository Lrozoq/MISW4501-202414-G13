import os
from dotenv import load_dotenv

load_dotenv()
DB_USER = os.getenv("DB_USER","prueba")
DB_PASSWORD = os.getenv("DB_PASSWORD","prueba")
DB_HOST = os.getenv("DB_HOST","localhost")
DB_NAME = os.getenv("DB_NAME","prueba")
DB_PORT = os.getenv("DB_PORT","5432")

DB_USER_REPLICA = os.getenv("DB_USER_REPLICA","prueba")
DB_PASSWORD_REPLICA = os.getenv("DB_PASSWORD_REPLICA","prueba")
DB_HOST_REPLICA = os.getenv("DB_HOST_REPLICA","localhost")
DB_NAME_REPLICA = os.getenv("DB_NAME_REPLICA","prueba")
DB_PORT_REPLICA = os.getenv("DB_PORT_REPLICA","5432")

