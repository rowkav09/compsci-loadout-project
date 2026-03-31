from dotenv import load_dotenv
import os

load_dotenv()

CSFLOAT_API_KEY = os.getenv("CSFLOAT_API_KEY")
BUFF_API_KEY = os.getenv("BUFF_API_KEY")
STEAM_API_KEY = os.getenv("STEAM_API_KEY")