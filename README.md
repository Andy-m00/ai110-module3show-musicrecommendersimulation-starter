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
  Numerical score comparison. Every song gets a specific score calculated from the users target score and its own attributes. The closer it is to the target, the more points it get, the more likely it is recommended. As of writing this im on my first draft but Id ideally like to prompt the user on how they interacted with the recommended song. Platforms like spotify and tiktok use this hybrid method of suggestion based on engagement patterns and content attributes(mood, energy, genre, etc). They also use a miriad of differnt algos to weigh which song should be ranked higher taking into consideration; the date of release, or the genre, or whether users with simlar profiles interacted with this music. This is why Id like to see if theres a simple way to determine if the user had a positive listening experience or if they skipped. These platforms also do a bunch of realtime algorithm adjustments that are happening concurrently along with more recommendation systems that determine rankings through user engagement potential and how willing and often the user trys to explrore music but, this program wont be that complex.

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
Loaded: 17 songs

Top 5 recommendations for Pop fan:

1. Sunrise City by Neon Echo
   Genre: pop | Mood: happy
   Match score: 4.38
   Why: Genre match (+2.0), Mood match (+1.0), Energy match (+0.98), Danceability preference (+0.40)

2. Gym Hero by Max Pulse
   Genre: pop | Mood: intense
   Match score: 3.31
   Why: Genre match (+2.0), Energy match (+0.87), Danceability preference (+0.44)

3. Rooftop Lights by Indigo Parade
   Genre: indie pop | Mood: happy
   Match score: 2.67
   Why: Related genre (+0.30), Mood match (+1.0), Energy match (+0.96), Danceability preference (+0.41)

4. Sunday Parade by Marigold Arcade
   Genre: disco | Mood: upbeat
   Match score: 1.59
   Why: Related mood (+0.20), Energy match (+0.92), Danceability preference (+0.47)

5. Open Road by Silver Atlas
   Genre: country | Mood: confident
   Match score: 1.36
   Why: Related mood (+0.10), Energy match (+0.91), Danceability preference (+0.35)

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. "genre": pop, "mood": happy, "energy": 0.8, "likes_acosutic": , "prefers_high_danceability": true 

#   2. "genre": lofi, "mood": chill, "energy": 0.5, "likes_acosutic": true, "prefers_high_tempo": false

#   3. "genre": rock, "mood": intense, "energy": 0.9, "likes_acosutic": false, "prefers_high_tempo": true
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
I got more accurate predictions for music that was not in the same genre when I put more weight on energy and less on genre, at least from intuition based eye test.
- What happened when you added tempo or valence to the score
I implemented those features early on but they proved less usefull as they were meant as sort of tie breakers for songs with similar top three attributes in larger data sets which this example doesnt use. It uses a small 17 song data set.
- How did your system behave for different types of users
It was pretty consistent. Genre, mood, and energy were the most important to the overall score and all the other attrbutes gave a small amount of extra points.
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
I learned that turning data into predictions is a textbook example of the law of diminishing returns. Any attempt to weed out bias and provide better recommendations required so much more work for such small incremental differences in a songs score. All of this work to make make better predictions for only me since whats considered a good recommendation is still incredibly subjective. Some users might place more importance on the mood of a song, or the lyrics, or its genre. The points system can be tuned perfectly to the algorithms. If the genre or mood types dont exist. Attribute like energy that use numeric values are subjective. It's all very complicated and I understand why platforms like spotify use hybrid attribute/interactive methods in their recommendation logic.

- about where bias or unfairness could show up in systems like this
Biases and unfairness cans show up anywhere theres imported data involved. What information you chose to include or run your program on will inevetiably spawn some kind of bias whether its from limited data, or to much data, or data that doesnt include specific info. Fine tuning the algorithms that go into these systems is also incredibly tough. In a system that doesnt collect user input like this one deciding the scoring logic spawns an incredible amount of bias and unfairness, because the author decides what a good recommendation looks like but the aren't every potential user.


