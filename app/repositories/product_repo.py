from sqlalchemy.orm import Session

from app.models.product import ProductModel


class ProductRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(ProductModel).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        return db.query(ProductModel).filter(ProductModel.id == product_id).first()

    @staticmethod
    def create(db: Session, product_data: dict):
        db_product = ProductModel(**product_data)
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def update(db: Session, db_product: ProductModel, update_data: dict):
        for key, value in update_data.items():
            if value is not None:
                setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
        return db_product

    @staticmethod
    def delete(db: Session, db_product: ProductModel):
        db.delete(db_product)
        db.commit()
