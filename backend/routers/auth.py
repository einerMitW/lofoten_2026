import os
from fastapi import APIRouter, HTTPException, Header, Depends
from pydantic import BaseModel

try:
    from backend import config
except ModuleNotFoundError:
    import config

router = APIRouter(prefix="/api/auth", tags=["auth"])

class LoginRequest(BaseModel):
    password: str

class LoginResponse(BaseModel):
    token: str
    status: str

def get_admin_password() -> str:
    return os.getenv("ADMIN_PASSWORD", config.ADMIN_PASSWORD)

def get_secret_key() -> str:
    return os.getenv("SECRET_KEY", config.SECRET_KEY)

def get_valid_token():
    return f"token_{get_secret_key()}"

def verify_token(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized")
    token = authorization.split(" ")[1]
    if token != get_valid_token():
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@router.post("/login", response_model=LoginResponse)
def login(req: LoginRequest):
    if req.password == get_admin_password():
        return LoginResponse(token=get_valid_token(), status="authenticated")
    raise HTTPException(status_code=401, detail="Invalid password")
