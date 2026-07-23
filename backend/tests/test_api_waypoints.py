import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_waypoints_empty_initial():
    response = client.get("/api/waypoints")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_waypoint_unauthorized():
    payload = {
        "title": "Reinebringen Peak",
        "description": "Stunning view over Reine",
        "lat": 67.9275,
        "lng": 13.0850,
        "image_path": "/api/images/reine.jpg"
    }
    response = client.post("/api/waypoints", json=payload)
    assert response.status_code == 401

def test_create_and_delete_waypoint_authorized():
    # Login first
    login_resp = client.post("/api/auth/login", json={"password": "lofoten2026admin"})
    token = login_resp.json()["token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    payload = {
        "title": "Reinebringen Peak",
        "description": "Stunning view over Reine",
        "lat": 67.9275,
        "lng": 13.0850,
        "image_path": "/api/images/reine.jpg"
    }
    
    # Create
    create_resp = client.post("/api/waypoints", json=payload, headers=headers)
    assert create_resp.status_code == 201
    created_data = create_resp.json()
    wp_id = created_data["id"]
    
    # Verify in list
    list_resp = client.get("/api/waypoints")
    assert len(list_resp.json()) >= 1
    
    # Delete
    del_resp = client.delete(f"/api/waypoints/{wp_id}", headers=headers)
    assert del_resp.status_code == 200
