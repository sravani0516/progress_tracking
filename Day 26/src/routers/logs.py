
from fastapi import APIRouter
from src.db.mongodb import logs_collection

router = APIRouter()

@router.get("/")
def get_logs():
    logs = list(logs_collection.find({}, {"_id": 0}))
    return logs
