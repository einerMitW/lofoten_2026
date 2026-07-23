from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional

try:
    from backend.database import DatabaseManager
    from backend.config import DB_PATH
    from backend.routers.auth import verify_token
    from backend.utils.sanitizer import sanitize_text
except ModuleNotFoundError:
    from database import DatabaseManager
    from config import DB_PATH
    from routers.auth import verify_token
    from utils.sanitizer import sanitize_text

router = APIRouter(prefix="/api/waypoints", tags=["waypoints"])
db = DatabaseManager(DB_PATH)
db.init_db()

class WaypointCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    lat: float
    lng: float
    image_path: Optional[str] = ""

@router.get("")
def list_waypoints():
    return db.get_all_waypoints()

@router.post("", status_code=201)
def create_waypoint(wp: WaypointCreate, token: str = Depends(verify_token)):
    clean_title = sanitize_text(wp.title)
    clean_desc = sanitize_text(wp.description or "")
    if not clean_title:
        raise HTTPException(status_code=400, detail="Title cannot be empty")
        
    wp_id = db.create_waypoint(
        title=clean_title,
        description=clean_desc,
        lat=wp.lat,
        lng=wp.lng,
        image_path=wp.image_path or ""
    )
    return {"id": wp_id, "title": clean_title, "lat": wp.lat, "lng": wp.lng}

@router.delete("/{waypoint_id}")
def delete_waypoint(waypoint_id: int, token: str = Depends(verify_token)):
    success = db.delete_waypoint(waypoint_id)
    if not success:
        raise HTTPException(status_code=404, detail="Waypoint not found")
    return {"status": "deleted", "id": waypoint_id}
