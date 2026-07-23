from fastapi import APIRouter, HTTPException, Header, Depends
from pydantic import BaseModel

try:
    from backend.config import ADMIN_PASSWORD, SECRET_KEY
except ModuleNotFoundError:
    from config import ADMIN_PASSWORD, SECRET_KEY

router = APIRouter(prefix="/api/auth", tags=["auth"])

class LoginRequest(BaseModel):
    password: str

class LoginResponse(BaseModel):
    token: str
    status: str

VALID_TOKEN = f"token_{SECRET_KEY}"

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ")[1]
    if token != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    if req.password == ADMIN_PASSWORD:
        return LoginResponse(token=VALID_TOKEN, status="authenticated")
    raise HTTPException(status_code=401, detail="Invalid password")
