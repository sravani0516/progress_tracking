
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.mysql import get_db
from src import crud, schemas

router = APIRouter()

@router.post("/", response_model=schemas.ProductResponse)
def create(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.get("/", response_model=list[schemas.ProductResponse])
def read_all(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_products(db, page, limit)

@router.get("/{product_id}", response_model=schemas.ProductResponse)
def read_one(product_id: int, db: Session = Depends(get_db)):
    return crud.get_product(db, product_id)

@router.put("/{product_id}", response_model=schemas.ProductResponse)
def update(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):
    return crud.delete_product(db, product_id)
