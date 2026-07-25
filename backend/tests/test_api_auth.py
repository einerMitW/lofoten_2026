import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_login_success():
    response = client.post("/api/auth/login", json={"password": "test_admin_pass"})
    assert response.status_code == 200
    data = response.json()
    assert "token" in data

def test_login_wrong_password():
    response = client.post("/api/auth/login", json={"password": "wrong_password"})
    assert response.status_code == 401
