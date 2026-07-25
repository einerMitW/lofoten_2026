import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_get_route_endpoint():
    response = client.get("/api/route")
    assert response.status_code == 200
    data = response.json()
    assert "geojson" in data
    assert "telemetry" in data
    assert data["geojson"]["type"] == "FeatureCollection"
    assert data["telemetry"]["total_distance_km"] > 0
