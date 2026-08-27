import os
from dotenv import load_dotenv

load_dotenv()

JOBS_DIR = os.getenv("JOBS_DIR", "./jobs")
MODELS_DIR = os.getenv("HEARTMULA_MODEL_PATH", "./models")
DEVICE = os.getenv("DEVICE", "mps")
DEFAULT_DURATION_MS = int(os.getenv("DEFAULT_DURATION_MS", "30000"))
