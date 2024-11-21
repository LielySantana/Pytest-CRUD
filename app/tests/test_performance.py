import time
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_category_performance():
    start = time.time()
    response = client.get("/categories/sizes")
    end = time.time()
    assert response.status_code == 200
    assert end - start < 1  
