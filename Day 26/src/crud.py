
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src import models
from src.db.mongodb import logs_collection
from datetime import datetime

def create_product(db: Session, product):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    logs_collection.insert_one({
        "action": "CREATE_PRODUCT",
        "product_id": db_product.id,
        "timestamp": datetime.utcnow()
    })

    return db_product

def get_products(db: Session, page: int, limit: int):
    return db.query(models.Product).offset((page-1)*limit).limit(limit).all()

def get_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def update_product(db: Session, product_id: int, updates):
    product = get_product(db, product_id)
    for key, value in updates.dict(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)

    logs_collection.insert_one({
        "action": "UPDATE_PRODUCT",
        "product_id": product.id,
        "timestamp": datetime.utcnow()
    })

    return product

def delete_product(db: Session, product_id: int):
    product = get_product(db, product_id)
    db.delete(product)
    db.commit()

    logs_collection.insert_one({
        "action": "DELETE_PRODUCT",
        "product_id": product_id,
        "timestamp": datetime.utcnow()
    })

    return {"message": "Product deleted"}
