"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs
from .rag import generate_playlist_guidence


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"\nLoaded songs: {len(songs)}\n")
    # Starter example profile
    user_prefs_1 = {"genre": "pop", "mood": "happy", "energy": 0.8}
    user_prefs_2 = {"genre": "rock", "mood": "intense", "energy": 0.9}
    user_prefs_3 = {"genre": "lofi", "mood": "chill", "energy": 0.4}

    all_prefs = [user_prefs_1, user_prefs_2, user_prefs_3]

    for i, prefs in enumerate(all_prefs, start=1):
        print(f"\n--- User {i}: {prefs} ---\n")
        recommendations = recommend_songs(prefs, songs, k=5)
        for rec in recommendations:
            song, score, explanation = rec
            print(f"{song['title']} - Score: {score:.2f}")
            print(f"Because: {explanation}")
            print()

        print("AI playlist guidence:")
        ai_text = generate_playlist_guidence(prefs, recommendations)
        print(ai_text)
        print()


if __name__ == "__main__":
    main()
