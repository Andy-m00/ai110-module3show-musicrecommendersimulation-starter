"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded: {len(songs)} songs")

    user_profiles = {
        "Pop fan": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.8,
            "prefers_high_danceability": True,
        },
        "Chill listener": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.5,
            "likes_acoustic": True,
            "prefers_high_tempo": False,
        },
        "deep intense rock":{
            "genre": "rock",
            "mood": "intense",
            "energy": 0.9,
            "likes_acoustic": False,
            "prefers_high_tempo": True,

        },
    }

    for profile_name, user_prefs in user_profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)

        print(f"\nTop {len(recommendations)} recommendations for {profile_name}:\n")
        if not recommendations:
            print("No recommendations found.")
            continue

        for number, (song, score, explanation) in enumerate(recommendations, start=1):
            print(f"{number}. {song['title']} by {song['artist']}")
            print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
            print(f"   Match score: {score:.2f}")
            if explanation:
                print(f"   Why: {explanation.replace('; ', ', ')}")
            print()

if __name__ == "__main__":
    main()
