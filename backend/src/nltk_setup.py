import sys
import nltk
from pathlib import Path

VENV_DIR = Path(sys.prefix)
NLTK_DATA_DIR = VENV_DIR / "nltk_data"
NLTK_DATA_DIR.mkdir(exist_ok=True)

if str(NLTK_DATA_DIR) not in nltk.data.path:
    nltk.data.path.append(str(NLTK_DATA_DIR))

REQUIRED_PACKAGES = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "omw-1.4",
]

import zipfile

def ensure_nltk_resources() -> None:
    """
    Check for required NLTK resources and download them if missing.
    Handles corrupted downloads (BadZipFile).
    """
    for pkg in REQUIRED_PACKAGES:
        missing = False
        try:
            try:
                nltk.data.find(f"tokenizers/{pkg}")
            except LookupError:
                nltk.data.find(f"corpora/{pkg}")
        except (LookupError, zipfile.BadZipFile):
            missing = True

        if missing:
            print(f"Downloading NLTK resource: {pkg}")
            try:
                nltk.download(pkg, download_dir=str(NLTK_DATA_DIR), quiet=True)
            except Exception as e:
                print(f"Failed to download {pkg}: {e}")

if __name__ == "__main__":
    ensure_nltk_resources()
