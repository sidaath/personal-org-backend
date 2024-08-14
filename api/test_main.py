from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

def test_get_init():
    response = client.get('/')
    assert response.json() == "helloooo"

