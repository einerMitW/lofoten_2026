def test_pytest_environment_works(temp_db, sample_gpx_content):
    """Verifies Pytest environment and test fixtures are operational."""
    assert temp_db is not None
    assert "<gpx" in sample_gpx_content
