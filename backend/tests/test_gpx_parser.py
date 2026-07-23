import pytest
import os
from backend.utils.gpx_parser import parse_gpx_file, parse_all_gpx_files, calculate_haversine_distance

def test_calculate_haversine_distance():
    dist = calculate_haversine_distance(67.9333, 13.0833, 67.8806, 12.9819)
    assert 6.5 <= dist <= 8.5

def test_parse_gpx_file(sample_gpx_content, tmp_path):
    gpx_file = tmp_path / "test.gpx"
    gpx_file.write_text(sample_gpx_content, encoding="utf-8")
    
    points, telemetry = parse_gpx_file(str(gpx_file))
    assert len(points) == 2
    assert points[0][:3] == [12.977, 67.877, 25.0]
    assert points[1][:3] == [12.980, 67.880, 50.0]
    assert telemetry["max_elevation"] == 50.0
    assert telemetry["min_elevation"] == 25.0
    assert telemetry["elevation_gain"] == 25.0
    assert telemetry["total_distance_km"] > 0

def test_gpx_stage_direction_auto_alignment(tmp_path):
    stage0 = """<?xml version="1.0"?>
<gpx version="1.1"><trk><trkseg>
  <trkpt lat="67.80" lon="12.80"><ele>10</ele></trkpt>
  <trkpt lat="67.85" lon="12.85"><ele>20</ele></trkpt>
</trkseg></trk></gpx>"""

    stage1_reversed = """<?xml version="1.0"?>
<gpx version="1.1"><trk><trkseg>
  <trkpt lat="67.90" lon="12.90"><ele>30</ele></trkpt>
  <trkpt lat="67.86" lon="12.86"><ele>25</ele></trkpt>
</trkseg></trk></gpx>"""

    gpx_dir = tmp_path / "gpx_dir"
    os.makedirs(gpx_dir, exist_ok=True)
    (gpx_dir / "gt_moskenesoya_0.gpx").write_text(stage0, encoding="utf-8")
    (gpx_dir / "gt_moskenesoya_1.gpx").write_text(stage1_reversed, encoding="utf-8")

    geojson, telemetry = parse_all_gpx_files(str(gpx_dir))
    features = geojson["features"]
    assert len(features) == 2

    stage1_coords = features[1]["geometry"]["coordinates"]
    assert stage1_coords[0][1] == 67.86

def test_cumulative_distance_monotonicity():
    gpx_dir = os.path.join(os.path.dirname(__file__), "..", "..", "GpxStorage")
    geojson, telemetry = parse_all_gpx_files(gpx_dir)
    
    prev_cum_dist = 0.0
    for feat in geojson["features"]:
        for pt in feat["geometry"]["coordinates"]:
            assert len(pt) >= 4  # [lon, lat, ele, cum_dist_km]
            cum_dist = pt[3]
            assert cum_dist >= prev_cum_dist
            prev_cum_dist = cum_dist

def test_parse_all_gpx_files_real_data():
    gpx_dir = os.path.join(os.path.dirname(__file__), "..", "..", "GpxStorage")
    geojson, telemetry = parse_all_gpx_files(gpx_dir)
    
    assert geojson["type"] == "FeatureCollection"
    assert len(geojson["features"]) > 0
    assert geojson["features"][0]["geometry"]["type"] == "LineString"
    assert telemetry["total_distance_km"] > 50
    assert telemetry["max_elevation"] > 200
    assert telemetry["elevation_gain"] > 500
