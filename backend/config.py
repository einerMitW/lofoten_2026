import os
from dotenv import load_dotenv

load_dotenv()

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
SECRET_KEY = os.getenv("SECRET_KEY")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GPX_STORAGE_DIR = os.path.join(BASE_DIR, "..", "GpxStorage")
IMAGE_STORAGE_DIR = os.path.join(BASE_DIR, "..", "ImageStorage")
DB_PATH = os.path.join(BASE_DIR, "data.db")

os.makedirs(IMAGE_STORAGE_DIR, exist_ok=True)
os.makedirs(GPX_STORAGE_DIR, exist_ok=True)
