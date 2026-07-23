from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

try:
    from backend.database import DatabaseManager
    from backend.config import DB_PATH
    from backend.routers import auth, gpx, waypoints, images
except ModuleNotFoundError:
    from database import DatabaseManager
    from config import DB_PATH
    from routers import auth, gpx, waypoints, images

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = DatabaseManager(DB_PATH)
    db.init_db()
    yield

app = FastAPI(title="Lofoten 2026 Trail API", version="1.0.0", lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(gpx.router)
app.include_router(waypoints.router)
app.include_router(images.router)

@app.get("/")
def root():
    return {"message": "Lofoten 2026 Trail API Operational"}
