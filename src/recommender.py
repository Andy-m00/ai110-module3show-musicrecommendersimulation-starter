import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

TEMPO_THRESHOLD_BPM = 120
TEMPO_MATCH_BONUS = 0.5
SUBGENRE_MATCH_POINTS = 1.5

SUBGENRES = {
    "electronic": {"edm", "house music"},
    "hip-hop": {"trap", "rap"},
    "country": {"traditional country", "modern country"},
    "latin": {"regional mexican", "reggaeton", "latin rock"},
}

RELATED_GENRES = {
    "acoustic": {"folk": 0.4, "bossa nova": 0.3},
    "folk": {"acoustic": 0.4, "country": 0.2},
    "bossa nova": {"acoustic": 0.3, "jazz": 0.2},
    "pop": {"indie pop": 0.3, "hip-pop": 0},
    "country": {"acoustic": 0.2, "folk": 0.2},
    "jazz": {"ambient": 0.2},
    "ambient": {"jazz": 0.2, "lofi": 0.4},
    "lofi": {"jazz": 0.2},
    "indie pop": {"pop": 0.3, "synthwave": 0.3},
    "electronic": {"disco": 0.2, "synthwave": 0.4},
    "disco": {"synthwave": 0.3},
    "rock": {"pop": 0.2},
    "synthwave": {"electronic": 0.3},
    "r&b": {},
}

RELATED_MOODS = {
    "happy": {"upbeat": 0.2, "hopeful": 0.1, "confident": 0.1},
    "upbeat": {"happy": 0.2, "confident": 0.1},
    "hopeful": {"happy": 0.1, "peaceful": 0.1},
    "confident": {"happy": 0.1, "upbeat": 0.1, "intense": 0.1},
    "intense": {"confident": 0.1},
    "chill": {"relaxed": 0.2, "peaceful": 0.1, "serene": 0.1, "focused": 0.1},
    "relaxed": {"chill": 0.2, "peaceful": 0.1, "serene": 0.1},
    "peaceful": {"relaxed": 0.1, "serene": 0.2, "chill": 0.1, "hopeful": 0.1},
    "serene": {"peaceful": 0.2, "chill": 0.1, "relaxed": 0.1},
    "focused": {"chill": 0.1},
    "moody": {"melancholy": 0.2},
    "melancholy": {"moody": 0.2},
    "curious": {"focused": 0.1},
}

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int 
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: Optional[bool] = None
    prefers_high_tempo: Optional[bool] = None
    prefers_high_danceability: Optional[bool] = None

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file."""
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        songs = list(csv.DictReader(csv_file))

    for song in songs:
        song["id"] = int(song["id"])
        for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
            song[field] = float(song[field])

    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score a song against user preferences and return matching reasons."""
    score = 0.0
    reasons = []

    song_genre = song["genre"].strip().casefold()
    preferred_genre = user_prefs["genre"].strip().casefold()

    if song_genre == preferred_genre:
        score += 2.0
        reasons.append("Genre match (+2.0)")
    else:
        if song_genre in SUBGENRES.get(preferred_genre, set()):
            score += SUBGENRE_MATCH_POINTS
            reasons.append(f"Subgenre match (+{SUBGENRE_MATCH_POINTS:.2f})")
        else:
            related_genre_points = RELATED_GENRES.get(preferred_genre, {}).get(
                song_genre, 0
            )
            score += related_genre_points
            if related_genre_points > 0:
                reasons.append(f"Related genre (+{related_genre_points:.2f})")

    if song["mood"] == user_prefs["mood"]:
        score += 1.0
        reasons.append("Mood match (+1.0)")
    else:
        related_mood_points = RELATED_MOODS.get(user_prefs["mood"], {}).get(
            song["mood"], 0
        )
        score += related_mood_points
        if related_mood_points > 0:
            reasons.append(f"Related mood (+{related_mood_points:.2f})")

    energy_points = max(0.0, 1.0 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_points
    if energy_points > 0:
        reasons.append(f"Energy match (+{energy_points:.2f})")

    if user_prefs.get("likes_acoustic") is True:
        acoustic_points = song["acousticness"] * 0.5
        score += acoustic_points
        if acoustic_points > 0:
            reasons.append(f"Acoustic preference (+{acoustic_points:.2f})")
    elif user_prefs.get("likes_acoustic") is False:
        acoustic_points = (1.0 - song["acousticness"]) * 0.5
        score += acoustic_points
        if acoustic_points > 0:
            reasons.append(f"Acoustic preference (+{acoustic_points:.2f})")

    prefers_high_tempo = user_prefs.get("prefers_high_tempo")
    if isinstance(prefers_high_tempo, bool):
        song_has_high_tempo = song["tempo_bpm"] >= TEMPO_THRESHOLD_BPM
        if song_has_high_tempo == prefers_high_tempo:
            score += TEMPO_MATCH_BONUS
            reasons.append(f"Tempo preference match (+{TEMPO_MATCH_BONUS:.2f})")

    prefers_high_danceability = user_prefs.get("prefers_high_danceability")
    if prefers_high_danceability is True:
        danceability_points = song["danceability"] * 0.5
        score += danceability_points
        if danceability_points > 0:
            reasons.append(f"Danceability preference (+{danceability_points:.2f})")
    elif prefers_high_danceability is False:
        danceability_points = (1.0 - song["danceability"]) * 0.5
        score += danceability_points
        if danceability_points > 0:
            reasons.append(f"Danceability preference (+{danceability_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Return the top-k songs ranked by preference score."""
    if k <= 0:
        return []

    scored_songs = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        scored_songs.append((song, score, "; ".join(reasons)))

    return sorted(scored_songs, key=lambda result: result[1], reverse=True)[:k]
