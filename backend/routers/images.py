import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import FileResponse

try:
    from backend.config import IMAGE_STORAGE_DIR
    from backend.routers.auth import verify_token
    from backend.utils.sanitizer import sanitize_filename
except ModuleNotFoundError:
    from config import IMAGE_STORAGE_DIR
    from routers.auth import verify_token
    from utils.sanitizer import sanitize_filename

router = APIRouter(prefix="/api/images", tags=["images"])

@router.post("")
async def upload_image(file: UploadFile = File(...), token: str = Depends(verify_token)):
    clean_filename = sanitize_filename(file.filename)
    if not clean_filename:
        raise HTTPException(status_code=400, detail="Invalid image extension or filename")
        
    unique_filename = f"{uuid.uuid4().hex[:8]}_{clean_filename}"
    file_path = os.path.join(IMAGE_STORAGE_DIR, unique_filename)
    
    contents = await file.read()
    with open(file_path, "wb") as f:
        f.write(contents)
        
    return {"url": f"/api/images/{unique_filename}", "filename": unique_filename}

@router.get("/{filename}")
def serve_image(filename: str):
    clean = sanitize_filename(filename)
    if not clean:
        raise HTTPException(status_code=400, detail="Invalid filename")
        
    file_path = os.path.join(IMAGE_STORAGE_DIR, clean)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Image not found")
        
    return FileResponse(file_path)
