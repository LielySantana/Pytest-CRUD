from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_item_deletion():
    response = client.post("/categories/sizes", json={"name": "Jacket", "description": "Warm jacket"})
    assert response.status_code == 200
    item_id = response.json()["id"]

    delete_response = client.delete(f"/categories/items/{item_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["id"] == item_id

    fetch_response = client.get("/categories/sizes")
    assert all(item["id"] != item_id for item in fetch_response.json())
