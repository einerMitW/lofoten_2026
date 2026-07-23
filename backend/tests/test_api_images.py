import pytest
import io
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_upload_image_unauthorized():
    files = {"file": ("test.jpg", b"fake image content", "image/jpeg")}
    response = client.post("/api/images", files=files)
    assert response.status_code == 401

def test_upload_image_invalid_extension():
    login_resp = client.post("/api/auth/login", json={"password": "lofoten2026admin"})
    token = login_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    files = {"file": ("malicious.exe", b"binary content", "application/octet-stream")}
    response = client.post("/api/images", files=files, headers=headers)
    assert response.status_code == 400

def test_upload_and_serve_image_success():
    login_resp = client.post("/api/auth/login", json={"password": "lofoten2026admin"})
    token = login_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    files = {"file": ("lofoten_view.jpg", b"fake jpeg byte data", "image/jpeg")}
    response = client.post("/api/images", files=files, headers=headers)
    assert response.status_code == 200
    image_url = response.json()["url"]
    
    # Retrieve static image
    serve_resp = client.get(image_url)
    assert serve_resp.status_code == 200
    assert serve_resp.content == b"fake jpeg byte data"
