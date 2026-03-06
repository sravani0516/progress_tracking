
from pymongo import MongoClient
from src.config import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
logs_collection = db["activity_logs"]
