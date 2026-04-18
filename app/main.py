from fastapi import FastAPI

from app.database.db_mysql import Base, engine
from app.routers import products

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(products.router)
