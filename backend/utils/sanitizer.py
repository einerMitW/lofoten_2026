import re
import os

ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}

def sanitize_text(text: str) -> str:
    """Strips HTML tags and script elements from input text."""
    if not text:
        return ""
    clean = re.sub(r'<[^>]*>', '', text)
    return clean.strip()

def sanitize_filename(filename: str) -> str | None:
    """Sanitizes filename and enforces safe image extensions."""
    if not filename:
        return None
    basename = os.path.basename(filename)
    basename = re.sub(r'[^a-zA-Z0-9_.-]', '_', basename)
    
    name, ext = os.path.splitext(basename)
    ext = ext.lower()
    if ext not in ALLOWED_EXTENSIONS:
        return None
        
    return f"{name}{ext}"

