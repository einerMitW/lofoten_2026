import sys
import os
import pytest
import tempfile
import sqlite3

# Ensure project root is in sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

@pytest.fixture(autouse=True)
def mock_env_variables(monkeypatch, tmp_path):
    """Isolates test environment variables, DB path, and image storage directory."""
    monkeypatch.setenv("ADMIN_PASSWORD", "test_admin_pass")
    monkeypatch.setenv("SECRET_KEY", "test_secret_key")
    
    # Isolated test database path
    test_db_path = str(tmp_path / "isolated_test_data.db")
    try:
        import backend.config as config
        monkeypatch.setattr(config, "DB_PATH", test_db_path)
    except ModuleNotFoundError:
        import config
        monkeypatch.setattr(config, "DB_PATH", test_db_path)

    # Isolated test image storage directory
    test_image_dir = str(tmp_path / "isolated_images")
    os.makedirs(test_image_dir, exist_ok=True)
    try:
        import backend.config as config
        monkeypatch.setattr(config, "IMAGE_STORAGE_DIR", test_image_dir)
        import backend.routers.images as images_router
        monkeypatch.setattr(images_router, "IMAGE_STORAGE_DIR", test_image_dir)
    except ModuleNotFoundError:
        import config
        monkeypatch.setattr(config, "IMAGE_STORAGE_DIR", test_image_dir)
        import routers.images as images_router
        monkeypatch.setattr(images_router, "IMAGE_STORAGE_DIR", test_image_dir)

@pytest.fixture
def temp_db(tmp_path):
    """Provides a temporary SQLite DB connection for testing."""
    test_db_file = str(tmp_path / "fixture_test.db")
    conn = sqlite3.connect(test_db_file)
    yield conn
    conn.close()

@pytest.fixture
def sample_gpx_content():
    """Provides sample GPX XML string for unit testing."""
    return """<?xml version="1.0"?>
<gpx version="1.1" creator="Test">
  <trk>
    <name>Test Track</name>
    <trkseg>
      <trkpt lat="67.877" lon="12.977"><ele>25.0</ele></trkpt>
      <trkpt lat="67.880" lon="12.980"><ele>50.0</ele></trkpt>
    </trkseg>
  </trk>
</gpx>
"""
