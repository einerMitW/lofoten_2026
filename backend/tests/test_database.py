import pytest
import sqlite3
from backend.database import DatabaseManager

def test_database_init_tables(tmp_path):
    db_file = str(tmp_path / "test_data.db")
    db = DatabaseManager(db_file)
    db.init_db()
    
    waypoints = db.get_all_waypoints()
    assert waypoints == []

def test_waypoint_crud_operations(tmp_path):
    db_file = str(tmp_path / "test_data.db")
    db = DatabaseManager(db_file)
    db.init_db()
    
    # Create
    wp_id = db.create_waypoint(
        title="Kvalvika Beach Camp",
        description="Beautiful bivouac under steep cliffs",
        lat=68.0442,
        lng=13.0931,
        image_path="/images/kvalvika.jpg"
    )
    assert wp_id is not None
    
    # Read
    waypoints = db.get_all_waypoints()
    assert len(waypoints) == 1
    assert waypoints[0]["title"] == "Kvalvika Beach Camp"
    assert waypoints[0]["lat"] == 68.0442
    assert waypoints[0]["lng"] == 13.0931
    assert waypoints[0]["image_path"] == "/images/kvalvika.jpg"
    
    # Delete
    deleted = db.delete_waypoint(wp_id)
    assert deleted is True
    assert db.get_all_waypoints() == []
