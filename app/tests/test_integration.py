from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    payload = {"name": "T-shirt", "description": "Red cotton t-shirt"}
    response = client.post("/categories/sizes", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "T-shirt"
    assert response.json()["category"] == "sizes"

def test_get_category():
    response = client.get("/categories/sizes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
