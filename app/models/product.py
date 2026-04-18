from sqlalchemy import Column, Float, Integer, String

from app.database.db_mysql import Base


class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(255))
    price = Column(Float)
    stock = Column(Integer)
