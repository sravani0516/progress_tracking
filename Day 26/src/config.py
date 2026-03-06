
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MYSQL_USER = os.getenv("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "root")
    MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
    MYSQL_DB = os.getenv("MYSQL_DB", "inventory_db")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017")
    MONGO_DB = os.getenv("MONGO_DB", "inventory_logs")

settings = Settings()
