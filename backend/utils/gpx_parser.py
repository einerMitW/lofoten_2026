import os
import math
import re
import gpxpy
import gpxpy.gpx
from typing import List, Tuple, Dict, Any

def calculate_haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculates distance in km between two lat/lon points using Haversine formula."""
    R = 6371.0  # Earth radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def parse_gpx_file(file_path: str) -> Tuple[List[List[float]], Dict[str, float]]:
    """Parses a single GPX file and returns track points [lon, lat, ele] and telemetry."""
    points: List[List[float]] = []
    total_distance_km = 0.0
    elevation_gain = 0.0
    max_elevation = -9999.0
    min_elevation = 9999.0
    
    with open(file_path, 'r', encoding='utf-8') as f:
        gpx = gpxpy.parse(f)
        
    prev_point = None
    for track in gpx.tracks:
        for segment in track.segments:
            for pt in segment.points:
                ele = pt.elevation if pt.elevation is not None else 0.0
                coords = [pt.longitude, pt.latitude, ele]
                points.append(coords)
                
                max_elevation = max(max_elevation, ele)
                min_elevation = min(min_elevation, ele)
                
                if prev_point is not None:
                    dist = calculate_haversine_distance(prev_point.latitude, prev_point.longitude, pt.latitude, pt.longitude)
                    total_distance_km += dist
                    
                    prev_ele = prev_point.elevation if prev_point.elevation is not None else 0.0
                    ele_diff = ele - prev_ele
                    if ele_diff > 0:
                        elevation_gain += ele_diff
                        
                prev_point = pt
                
    if not points:
        max_elevation = 0.0
        min_elevation = 0.0
        
    telemetry = {
        "total_distance_km": round(total_distance_km, 2),
        "elevation_gain": round(elevation_gain, 1),
        "max_elevation": round(max_elevation, 1),
        "min_elevation": round(min_elevation, 1)
    }
    
    return points, telemetry

def _extract_sort_key(filename: str) -> float:
    """Extracts stage number from filenames like gt_moskenesoya_2_1.gpx -> 2.1."""
    match = re.search(r'_(\d+(?:_\d+)?)\.gpx$', filename)
    if match:
        num_str = match.group(1).replace('_', '.')
        return float(num_str)
    return 999.0

def parse_all_gpx_files(gpx_directory: str) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Parses all GPX files in directory in stage order and aggregates them into a GeoJSON FeatureCollection."""
    if not os.path.exists(gpx_directory):
        return {"type": "FeatureCollection", "features": []}, {
            "total_distance_km": 0.0,
            "elevation_gain": 0.0,
            "max_elevation": 0.0,
            "min_elevation": 0.0
        }
        
    files = [f for f in os.listdir(gpx_directory) if f.endswith('.gpx')]
    files.sort(key=_extract_sort_key)
    
    all_points: List[List[float]] = []
    total_distance = 0.0
    total_gain = 0.0
    max_ele = -9999.0
    min_ele = 9999.0
    
    features = []
    
    for filename in files:
        file_path = os.path.join(gpx_directory, filename)
        points, telemetry = parse_gpx_file(file_path)
        if points:
            all_points.extend(points)
            total_distance += telemetry["total_distance_km"]
            total_gain += telemetry["elevation_gain"]
            max_ele = max(max_ele, telemetry["max_elevation"])
            min_ele = min(min_ele, telemetry["min_elevation"])
            
            features.append({
                "type": "Feature",
                "properties": {
                    "stage": filename,
                    "distance_km": telemetry["total_distance_km"],
                    "elevation_gain": telemetry["elevation_gain"]
                },
                "geometry": {
                    "type": "LineString",
                    "coordinates": points
                }
            })
            
    if max_ele == -9999.0:
        max_ele = 0.0
        min_ele = 0.0
        
    overall_telemetry = {
        "total_distance_km": round(total_distance, 2),
        "elevation_gain": round(total_gain, 1),
        "max_elevation": round(max_ele, 1),
        "min_elevation": round(min_ele, 1),
        "stage_count": len(files)
    }
    
    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return geojson, overall_telemetry
