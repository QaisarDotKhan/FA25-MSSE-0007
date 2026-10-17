import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Student App")
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")
MAX_STUDENTS = int(os.getenv("MAX_STUDENTS", 100))
API_KEY = os.getenv("API_KEY")