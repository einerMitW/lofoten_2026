from fastapi import APIRouter

try:
    from backend.config import GPX_STORAGE_DIR
    from backend.utils.gpx_parser import parse_all_gpx_files
except ModuleNotFoundError:
    from config import GPX_STORAGE_DIR
    from utils.gpx_parser import parse_all_gpx_files

router = APIRouter(prefix="/api/route", tags=["route"])

@router.get("")
def get_aggregated_route():
    geojson, telemetry = parse_all_gpx_files(GPX_STORAGE_DIR)
    return {
        "geojson": geojson,
        "telemetry": telemetry
    }
