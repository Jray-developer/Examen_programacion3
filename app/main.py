from fastapi import FastAPI

from app.database.db_mysql import Base, engine
from app.routers import users

app = FastAPI()


@app.on_event("startup")
def configure_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"No se pudo conectar a MySQL: {e}")


app.include_router(users.router)
