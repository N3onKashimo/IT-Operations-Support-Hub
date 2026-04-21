from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

def load_csv(filename: str) -> pd.DataFrame:
    file_path = DATA_DIR / filename
    try:
        return pd.read_csv(file_path)
    except Exception:
        return pd.DataFrame()