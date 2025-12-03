
"""
Configuration file for Bank Reviews Analysis Project
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve project root (two levels up from this file: src/ -> project root)
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from project root .env if present
load_dotenv(dotenv_path=BASE_DIR / ".env")

# Google Play Store App IDs (can be overridden via .env)
APP_IDS = {
    'CBE': os.getenv('CBE_APP_ID', 'com.combanketh.mobilebanking'),
    'BOA': os.getenv('BOA_APP_ID', 'com.boa.boaMobileBanking'),
    'Dashenbank': os.getenv('DASHENBANK_APP_ID', 'com.dashen.dashensuperapp')
}

# Bank Names Mapping
BANK_NAMES = {
    'CBE': 'Commercial Bank of Ethiopia',
    'BOA': 'Bank of Abyssinia',
    'Dashenbank': 'Dashen Bank'
}

# Scraping Configuration
SCRAPING_CONFIG = {
    'reviews_per_bank': int(os.getenv('REVIEWS_PER_BANK', 400)),
    'max_retries': int(os.getenv('MAX_RETRIES', 3)),
    'lang': 'en',
    'country': 'et'  # Ethiopia
}

# File Paths (resolved relative to project root)
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

DATA_PATHS = {
    'base': str(DATA_DIR),
    'raw': str(RAW_DIR),
    'processed': str(PROCESSED_DIR),
    'raw_reviews': str(RAW_DIR / "reviews_raw.csv"),
    'processed_reviews': str(PROCESSED_DIR / "reviews_processed.csv"),
    'sentiment_results': str(PROCESSED_DIR / "reviews_with_sentiment.csv"),
    'final_results': str(PROCESSED_DIR / "reviews_final.csv")
}

# Ensure directories exist
os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)
