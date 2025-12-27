import sys
import os
import nltk
from pathlib import Path
import zipfile

def is_virtual_env() -> bool:
    """Check if running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def is_writable(path: Path) -> bool:
    """Check if a path is writable."""
    try:
        path.mkdir(parents=True, exist_ok=True)
        test_file = path / ".write_test"
        test_file.touch()
        test_file.unlink()
        return True
    except (PermissionError, OSError):
        return False


def get_nltk_data_dir() -> Path:
    """
    Get the appropriate NLTK data directory based on environment.
    
    Priority:
    1. NLTK_DATA environment variable (if set)
    2. Virtual environment directory (if in venv and writable)
    3. User home directory (fallback for containers/HF Spaces)
    """
    if os.environ.get("NLTK_DATA"):
        env_path = Path(os.environ["NLTK_DATA"])
        if is_writable(env_path):
            return env_path
    
    if is_virtual_env():
        venv_path = Path(sys.prefix) / "nltk_data"
        if is_writable(venv_path):
            return venv_path
    
    home_path = Path.home() / "nltk_data"
    if is_writable(home_path):
        return home_path
    
    local_path = Path.cwd() / "nltk_data"
    return local_path


NLTK_DATA_DIR = get_nltk_data_dir()
NLTK_DATA_DIR.mkdir(parents=True, exist_ok=True)

if str(NLTK_DATA_DIR) not in nltk.data.path:
    nltk.data.path.insert(0, str(NLTK_DATA_DIR))

REQUIRED_PACKAGES = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "omw-1.4",
]

def ensure_nltk_resources() -> None:
    """
    Check for required NLTK resources and download them if missing.
    Handles corrupted downloads (BadZipFile).
    """
    print(f"NLTK data directory: {NLTK_DATA_DIR}")
    print(f"Environment: {'virtualenv' if is_virtual_env() else 'system/container'}")
    
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
        else:
            print(f"NLTK resource already exists: {pkg}")
    
    print("NLTK setup complete!")


if __name__ == "__main__":
    ensure_nltk_resources()