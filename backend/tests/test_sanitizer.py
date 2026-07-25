import pytest
from backend.utils.sanitizer import sanitize_text, sanitize_filename

def test_sanitize_text_html_stripping():
    raw_input = "<script>alert('xss')</script><b>Hello</b> Lofoten"
    clean = sanitize_text(raw_input)
    assert "<script>" not in clean
    assert "<b>" not in clean
    assert "Hello Lofoten" in clean

def test_sanitize_filename_prevents_path_traversal():
    malicious_filename = "../../../etc/passwd.jpg"
    clean = sanitize_filename(malicious_filename)
    assert ".." not in clean
    assert clean.endswith(".jpg")

def test_sanitize_filename_allowed_extensions():
    assert sanitize_filename("my_photo.PNG").endswith(".png")
    assert sanitize_filename("my_photo.WEBP").endswith(".webp")
    assert sanitize_filename("script.sh") is None
