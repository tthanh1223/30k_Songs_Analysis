"""Download the raw dataset into data/raw/.

Usage (from the project root):
    python -m src.download_data
"""
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"

# 30000 Spotify Songs - TidyTuesday 2020-01-21 (collected with the spotifyr R package)
SOURCES = {
    "spotify_songs.csv": (
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/"
        "master/data/2020/2020-01-21/spotify_songs.csv"
    ),
}


def download(name: str, url: str, force: bool = False) -> Path:
    path = RAW_DIR / name
    if path.exists() and not force:
        print(f"skip  {path.relative_to(ROOT)} (already exists)")
        return path
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    path.write_bytes(resp.content)
    print(f"saved {path.relative_to(ROOT)} ({len(resp.content) / 1e6:.1f} MB)")
    return path


if __name__ == "__main__":
    for name, url in SOURCES.items():
        download(name, url)
