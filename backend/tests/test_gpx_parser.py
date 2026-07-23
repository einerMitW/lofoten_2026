import pytest
import os
from backend.utils.gpx_parser import parse_gpx_file, parse_all_gpx_files, calculate_haversine_distance

def test_calculate_haversine_distance():
    # Distance between Reine (67.9333, 13.0833) and Å (67.8806, 12.9819) is approx 7.3 km
    dist = calculate_haversine_distance(67.9333, 13.0833, 67.8806, 12.9819)
    assert 6.5 <= dist <= 8.5

def test_parse_gpx_file(sample_gpx_content, tmp_path):
    gpx_file = tmp_path / "test.gpx"
    gpx_file.write_text(sample_gpx_content, encoding="utf-8")
    
    points, telemetry = parse_gpx_file(str(gpx_file))
    assert len(points) == 2
    assert points[0] == [12.977, 67.877, 25.0]
    assert points[1] == [12.980, 67.880, 50.0]
    assert telemetry["max_elevation"] == 50.0
    assert telemetry["min_elevation"] == 25.0
    assert telemetry["elevation_gain"] == 25.0
    assert telemetry["total_distance_km"] > 0

def test_parse_all_gpx_files_real_data():
    gpx_dir = os.path.join(os.path.dirname(__file__), "..", "..", "GpxStorage")
    geojson, telemetry = parse_all_gpx_files(gpx_dir)
    
    assert geojson["type"] == "FeatureCollection"
    assert len(geojson["features"]) > 0
    assert geojson["features"][0]["geometry"]["type"] == "LineString"
    assert telemetry["total_distance_km"] > 50  # Lofoten full trail is >50km
    assert telemetry["max_elevation"] > 200
    assert telemetry["elevation_gain"] > 500
