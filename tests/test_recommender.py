from src.recommender import Song, UserProfile, Recommender, score_song

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    # Starter expectation: the pop, happy, high energy song should score higher
    assert results[0].genre == "pop"
    assert results[0].mood == "happy"


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert explanation.strip() != ""


def test_optional_profile_preferences_default_to_unset():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
    )

    assert user.likes_acoustic is None
    assert user.prefers_high_tempo is None
    assert user.prefers_high_danceability is None


def test_high_danceability_preference_uses_proportional_score():
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "prefers_high_danceability": True,
    }
    high_danceability_song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.8,
    }

    score, reasons = score_song(user_prefs, high_danceability_song)

    assert score == 4.4
    assert "Danceability preference (+0.40)" in reasons


def test_low_danceability_preference_rewards_lower_values():
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "prefers_high_danceability": False,
    }
    low_danceability_song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.2,
    }

    score, reasons = score_song(user_prefs, low_danceability_song)

    assert score == 4.4
    assert "Danceability preference (+0.40)" in reasons


def test_danceability_preference_is_ignored_when_not_set():
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "danceability": 0.9,
    }

    score, reasons = score_song(user_prefs, song)

    assert score == 4.0
    assert not any("Danceability" in reason for reason in reasons)


def test_latin_subgenres_get_subgenre_score():
    user_prefs = {"genre": "latin", "mood": "neutral", "energy": 1.0}

    for genre in ("regional mexican", "reggaeton", "latin rock"):
        score, reasons = score_song(
            user_prefs, {"mood": "neutral", "energy": 0.0, "genre": genre}
        )
        assert score == 2.5
        assert "Subgenre match (+1.50)" in reasons


def test_electronic_subgenres_get_subgenre_score():
    user_prefs = {"genre": "electronic", "mood": "neutral", "energy": 1.0}

    for genre in ("edm", "EDM", "house music"):
        score, reasons = score_song(
            user_prefs, {"genre": genre, "mood": "neutral", "energy": 0.0}
        )
        assert score == 2.5
        assert "Subgenre match (+1.50)" in reasons


def test_hip_hop_subgenres_get_subgenre_score():
    user_prefs = {"genre": "hip-hop", "mood": "neutral", "energy": 1.0}

    for genre in ("trap", "rap"):
        score, reasons = score_song(
            user_prefs, {"genre": genre, "mood": "neutral", "energy": 0.0}
        )
        assert score == 2.5
        assert "Subgenre match (+1.50)" in reasons


def test_country_subgenres_get_subgenre_score():
    user_prefs = {"genre": "country", "mood": "neutral", "energy": 1.0}

    for genre in ("traditional country", "modern country"):
        score, reasons = score_song(
            user_prefs, {"genre": genre, "mood": "neutral", "energy": 0.0}
        )
        assert score == 2.5
        assert "Subgenre match (+1.50)" in reasons


def test_tempo_preference_uses_120_bpm_threshold():
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "prefers_high_tempo": True,
    }
    song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "tempo_bpm": 120,
    }

    score, reasons = score_song(user_prefs, song)

    assert score == 4.5
    assert "Tempo preference match (+0.50)" in reasons


def test_low_tempo_preference_matches_songs_below_120_bpm():
    user_prefs = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "prefers_high_tempo": False,
    }
    song = {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.8,
        "tempo_bpm": 119,
    }

    score, reasons = score_song(user_prefs, song)

    assert score == 4.5
    assert "Tempo preference match (+0.50)" in reasons
