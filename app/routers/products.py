from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db_mysql import get_db
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    return ProductService.get_products(db)


@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return ProductService.create_product(db, product)


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int, product: ProductUpdate, db: Session = Depends(get_db)
):
    return ProductService.update_product(db, product_id, product)


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    return ProductService.delete_product(db, product_id)
