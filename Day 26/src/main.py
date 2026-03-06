
from fastapi import FastAPI
from src.db.mysql import Base, engine
from src.routers import products, logs

app = FastAPI(title="Cloud Inventory System")

Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
