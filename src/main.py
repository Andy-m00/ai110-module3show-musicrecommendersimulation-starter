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

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=15)

    print(f"\nTop {len(recommendations)} recommendations:\n")
    if not recommendations:
        print("No recommendations found.")
        return

    for number, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{number}. {song['title']} by {song['artist']}")
        print(f"   Genre: {song['genre']} | Mood: {song['mood']}")
        print(f"   Match score: {score:.2f}")
        if explanation:
            print(f"   Why: {explanation.replace('; ', ', ')}")
        print()


if __name__ == "__main__":
    main()
