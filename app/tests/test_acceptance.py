from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_and_fetch_item():
    payload = {"name": "Jeans", "description": "Blue denim jeans"}
    create_response = client.post("/categories/types", json=payload)
    assert create_response.status_code == 200

    fetch_response = client.get("/categories/types")
    assert fetch_response.status_code == 200
    assert any(item["name"] == "Jeans" for item in fetch_response.json())
