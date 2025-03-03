import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Define directories
PARENT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PARENT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
TRANSFORMED_DATA_DIR = DATA_DIR / "transformed"
MODELS_DIR = PARENT_DIR / "models"

# Create directories if they don't exist
for directory in [
    DATA_DIR,
    RAW_DATA_DIR,
    PROCESSED_DATA_DIR,
    TRANSFORMED_DATA_DIR,
    MODELS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)

FEATURE_GROUP_NAME = "time_series_hourly_feature_group"

FEATURE_GROUP_VERSION = 1

HOPSWORK_PROJECT_NAME = "MLOPS_End_To_End_Project"

HOPSWORK_API_KEY = "Vxuemktxr8Y2bSKW.QKTEM9sowmt0sCp2UUUX67xbl3rBGqDklkV7m19JjImPCQhkK5syM3mwYOND10RJ"