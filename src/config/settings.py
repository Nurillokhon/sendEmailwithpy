import os

from dotenv import load_dotenv
from pathlib import Path

# .env faylni to‘g‘ri yo‘l bilan yuklash
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SERVER_HOST = os.getenv("SERVER_HOST", "localhost")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS").split(",")
IS_ALLOWED_CREDENTIALS = os.getenv("IS_ALLOWED_CREDENTIALS", "true").lower() == "true"
ALLOWED_METHODS = os.getenv("ALLOWED_METHODS").split(",")
ALLOWED_HEADERS = os.getenv("ALLOWED_HEADERS").split(",")
