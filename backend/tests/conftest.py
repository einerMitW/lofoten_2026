import sys
import os
import pytest
import tempfile
import sqlite3

# Ensure the parent directory of backend (project root) is in sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


@pytest.fixture
def temp_db():
    """Provides a temporary in-memory or file-backed SQLite DB for testing."""
    conn = sqlite3.connect(":memory:")
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
