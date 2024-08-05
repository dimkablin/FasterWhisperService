import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

MODEL = os.getenv("WHISPER_MODEL", "small")
WEIGHTS_PATH = os.getenv("WEIGHTS_PATH", "whisper/weights")
PORT = int(os.getenv("WHISPER_PORT", 8000))
ADDRESS = os.getenv("WHISPER_ADDRESS", "0.0.0.0")
