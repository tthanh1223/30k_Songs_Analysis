"""Shared loading and cleaning, following the decisions in 01a section 2.1.

Usage in a notebook (notebooks/ is the working directory):

    import sys; sys.path.append('..')
    from src.load import load_raw, load_tracks, load_track_genres

    raw = load_raw()            # 32,833 rows: one row = track x playlist x subgenre
    tracks = load_tracks()      # 28,356 rows: one row = one track
    tg = load_track_genres()    # one row = one (track, genre) pair

Every function prints the row count before and after each step that changes the data.
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_CSV = ROOT / "data" / "raw" / "spotify_songs.csv"

AUDIO_COLS = [
    "danceability", "energy", "loudness", "speechiness", "acousticness",
    "instrumentalness", "liveness", "valence", "tempo", "duration_ms",
]
CATEGORY_COLS = ["key", "mode", "playlist_genre", "playlist_subgenre"]
# Columns that are identical for every row of the same track_id (checked in 01a, 2.1)
TRACK_LEVEL_COLS = [
    "track_name", "track_artist", "track_popularity", "track_album_id",
    "track_album_name", "release_year", "date_precision", "key", "mode",
] + AUDIO_COLS


def _report(step: str, before: int, after: int, verbose: bool) -> None:
    if verbose:
        print(f"{step}: {before:,} -> {after:,} rows")


def load_raw(path: Path = RAW_CSV, verbose: bool = True) -> pd.DataFrame:
    """Raw rows with fixed types. No rows removed.

    - track_album_release_date -> release_year (int) + date_precision ('day' | 'month' | 'year')
    - key, mode, playlist_genre, playlist_subgenre -> category
    - drops playlist_name (one name maps to up to 5 playlist_id) and the raw date string
    """
    df = pd.read_csv(path)
    n = len(df)

    date = df["track_album_release_date"]
    df["date_precision"] = date.str.len().map({10: "day", 7: "month", 4: "year"})
    df["release_year"] = date.str[:4].astype(int)
    df = df.drop(columns=["track_album_release_date", "playlist_name"])

    for col in CATEGORY_COLS:
        df[col] = df[col].astype("category")

    _report("load_raw", n, len(df), verbose)
    return df


def load_tracks(genre_rule: str = "most_frequent", verbose: bool = True) -> pd.DataFrame:
    """One row per track_id.

    Added columns (computed before collapsing, otherwise they are lost):
    - n_playlists: number of distinct playlists containing the track
    - n_genres: number of distinct playlist_genre values of the track
    - genre: one genre per track, chosen by `genre_rule`

    genre_rule (the group still has to agree on this, see 2.6):
    - "most_frequent": genre that appears in the most rows of the track; ties -> first in file order
    - "first": genre of the first row in file order
    - "single_only": keep only tracks with exactly one genre (drops multi-genre tracks)
    """
    df = load_raw(verbose=verbose)
    n = len(df)

    g = df.groupby("track_id", sort=False, observed=True)
    extra = pd.DataFrame({
        "n_playlists": g["playlist_id"].nunique(),
        "n_genres": g["playlist_genre"].nunique(),
    })

    if genre_rule == "most_frequent":
        counts = (df.groupby(["track_id", "playlist_genre"], sort=False, observed=True)
                    .size().rename("rows").reset_index())
        counts["order"] = counts.groupby("track_id").cumcount()   # file order of first appearance
        best = (counts.sort_values(["track_id", "rows", "order"], ascending=[True, False, True])
                      .drop_duplicates("track_id"))
        extra["genre"] = best.set_index("track_id")["playlist_genre"]
    elif genre_rule in ("first", "single_only"):
        extra["genre"] = g["playlist_genre"].first()
    else:
        raise ValueError(f"unknown genre_rule: {genre_rule}")

    tracks = df.drop_duplicates("track_id")[["track_id"] + TRACK_LEVEL_COLS]
    _report("load_tracks: one row per track_id", n, len(tracks), verbose)

    tracks = tracks.merge(extra, left_on="track_id", right_index=True, how="left",
                          validate="one_to_one")

    if genre_rule == "single_only":
        before = len(tracks)
        tracks = tracks[tracks["n_genres"] == 1]
        _report("load_tracks: keep single-genre tracks", before, len(tracks), verbose)

    tracks["genre"] = tracks["genre"].astype(df["playlist_genre"].dtype)
    return tracks.reset_index(drop=True)


def load_track_genres(verbose: bool = True) -> pd.DataFrame:
    """One row per (track_id, playlist_genre): a track counts once inside each genre.

    Use for genre comparisons; a multi-genre track appears once in each of its genres.
    """
    df = load_raw(verbose=verbose)
    n = len(df)
    tg = df.drop_duplicates(["track_id", "playlist_genre"])
    tg = tg[["track_id", "playlist_genre"] + TRACK_LEVEL_COLS].reset_index(drop=True)
    _report("load_track_genres: one row per (track, genre)", n, len(tg), verbose)
    return tg
