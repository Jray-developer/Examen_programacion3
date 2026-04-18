from fastapi import HTTPException

from app.repositories.product_repo import ProductRepository


class ProductService:
    @staticmethod
    def get_products(db):
        return ProductRepository.get_all(db)

    @staticmethod
    def create_product(db, product_schema):
        if product_schema.price < 0:
            raise HTTPException(
                status_code=400, detail="El precio no puede ser negativo"
            )
        return ProductRepository.create(db, product_schema.model_dump())

    @staticmethod
    def update_product(db, product_id, update_schema):
        product = ProductRepository.get_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        return ProductRepository.update(db, product, update_schema.model_dump())

    @staticmethod
    def delete_product(db, product_id):
        product = ProductRepository.get_by_id(db, product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Producto no encontrado")
        ProductRepository.delete(db, product)
        return {"message": "Producto eliminado exitosamente"}
