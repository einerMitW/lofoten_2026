import sqlite3
import os
from typing import List, Dict, Any, Optional

class DatabaseManager:
    def __init__(self, db_path: str = "data.db"):
        self.db_path = db_path

    def get_connection(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        """Initializes SQLite tables if they do not exist."""
        with self.get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS waypoints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    lat REAL NOT NULL,
                    lng REAL NOT NULL,
                    image_path TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            conn.commit()

    def get_all_waypoints(self) -> List[Dict[str, Any]]:
        """Returns all waypoints as a list of dicts."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, description, lat, lng, image_path, created_at FROM waypoints ORDER BY created_at ASC")
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def create_waypoint(self, title: str, description: str, lat: float, lng: float, image_path: str) -> int:
        """Inserts a new waypoint record and returns its ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO waypoints (title, description, lat, lng, image_path) VALUES (?, ?, ?, ?, ?)",
                (title, description, lat, lng, image_path)
            )
            conn.commit()
            return cursor.lastrowid

    def delete_waypoint(self, waypoint_id: int) -> bool:
        """Deletes a waypoint by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM waypoints WHERE id = ?", (waypoint_id,))
            conn.commit()
            return cursor.rowcount > 0

    def get_waypoint_by_id(self, waypoint_id: int) -> Optional[Dict[str, Any]]:
        """Fetches a single waypoint by ID."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, title, description, lat, lng, image_path, created_at FROM waypoints WHERE id = ?", (waypoint_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
