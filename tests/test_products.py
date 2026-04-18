from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.db_mysql import Base, get_db
from app.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


def test_create_and_read_product():
    Base.metadata.create_all(bind=engine)

    payload = {"name": "Test", "description": "Desc", "price": 10.5, "stock": 5}
    response = client.post("/products/", json=payload)
    assert response.status_code == 200

    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0
