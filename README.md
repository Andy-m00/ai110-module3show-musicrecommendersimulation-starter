# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Explain your design in plain language.

### Two starter workflows

- `src/main.py` uses the function-based workflow: songs are loaded from the CSV as a list of dictionaries and passed to functions such as `recommend_songs`.
- `tests/test_recommender.py` tests the object-oriented workflow: `Song` and `UserProfile` objects are used with the `Recommender` class.

These are separate ways to represent and recommend songs; the dictionary-based workflow does not automatically create `Song` objects.

Some prompts to answer:

- What features does each `Song` use in your system
  id,title,artist,genre,mood,energy,tempo_bpm,valence,danceability,acousticness
- What information does your `UserProfile` store
  favorite genre, favorite mood, target energy, plus optional acoustic, high/low tempo (120 BPM cutoff), and high/low danceability (0.7 cutoff) preferences
- How does your `Recommender` compute a score for each song
 it asigns a numerical value to each song based on how the songs listed attributes align with users "taste profile".
- How do you choose which songs to recommend
  Numerical score comparison. Every song gets a specific score calculated from the users target score and its own attributes. The closer it is to the target the more points it get the more likely it is recommended. As of writing this im on my first draft but Id ideally like to maybe prompt the user on how they interacted with the recommended song. Platforms like spotify and tiktok use this hybrid method of suggestion based on engagement patterns and content attributes(mood, energy, genre, etc). They also use a miriad of differnt algos to weigh which song should be ranked higher taking into consideration; the date of release, or the genre, or whether users with simlar profiles interacted with this music. This is why Id like to see if theres a simple way to determine if the user had a positive listening experience or if they skipped. These platforms also do a bunch of realtime algorithm adjustments that are happening concurrently along with more recommendation systems that determine rankings through user engagement potential and how willing and often the user trys to explrore music but, this program wont be that complex.

You can include a simple diagram or bullet list if helpful.
song is compared to users taste profile --> given a score --> list is created in order with error handling(matching attributes, same song etc) -->
---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
