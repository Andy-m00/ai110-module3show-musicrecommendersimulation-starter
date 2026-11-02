# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **music recomender 1.0** 

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
It generates recommendations based on the users preferences and how they align with the songs attributes. It compares them and then assigns points based on programable or authorable values in the code.
- What assumptions does it make about the user
It makes assumptions that they care equally about genre and energy and less about a songs mood and other interger values like tempo or valence. 
- Is this for real users or classroom exploration  
Its for classroom exploration. This program has aspects of the content recommendation algorithms premier commercial platoforms like tiktok, spotify and youtube have but it is nowhere near as complex.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.) 
Features like mood, genre, and energy are a must since they provide the bulk of the points a song gets. Song attributes like danceability, tempo preference, and accosuticness carry mush less weight in the final score of a song and hence its location in the recommendation list.
- What user preferences are considered  
Their favorite genre and mood, the energy out from 0.0 to 1.0 that they look for in music, yes or no on whether they like acousticness, danceability or high tempo.
- How does the model turn those into a score 
it gives a flat out set number of points(GENRE_MATCH_POINTS) for genre matches, mood matches. it also gives partial points when their aren't direct matches. theses relationships and how many points they reward are held in RELATED_ and SUBGENRE dictionaries. Energy takes the absolute difference from the song and the users energy value, and then subtracts it by 1.0(intended to reward less differnce), and then multipies that value by a changable multiplier(in this iteration its 1.5)
- What changes did you make from the starter logic 
I adjusted all the scoring values.

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
17 songs in the catalog.
- What genres or moods are represented 
13 different genres, 4 subgenres, and 12 different moods 
- Did you add or remove data  
I added 7 more songs and I think one more attribute.
- Are there parts of musical taste missing in the dataset  
Many parts of muscial taste missing in the dataset.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
Users who generally like pop and lofi msuic along with positive and chill moods from my perspective give the most reasonable results.
- Any patterns you think your scoring captures correctly  
I think it captures how likely someone looking for msuic within the same genre and energy level would like
- Cases where the recommendations matched your intuition  
Fans of chill lofi music were recommended more ambient chill music like jazz and low tempo sythnwave.
---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider
it importantly does not consider valence, lyrics or user interactions like; skips and listens and other stuff like that.
- Genres or moods that are underrepresented 
Half of the 17 song list only had one instance from the 16 genres represented. Also it lacks dozens of subgenres that i tried to fill in but stopped when i realized the dictionaries section was getting a bit to crowded.
- Cases where the system overfits to one preference  
There are about 3 lofi songs so its easy to see how well the scoring logic caters to that genre. Additionally I added a related genre feature that awards a number of partial points according to my personal biases of how genres relate to each other and I can see it causing some data skews. in this iteration, pop has a lot of related genres that award many songs partial points to songs that I think would have a similar genre vibe.
- Ways the scoring might unintentionally favor some users  
If a user likes lofi or pop or positive moods they'll get a more accurate recommendation at least according to my hand entered partial points values that are based completely on my personal biases.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested 
I tested "deep intense rock", "high enrgy pop fan", and  "chill listner"
- What you looked for in the recommendations  
I looked for genre matches, mood matches, and energy matches to be the real determining factor in reccomendations. Recommendations order after that was when the real nuance in the scoring logic came in. I implemented the whole partial points and subgenre scoring specifically to try to make more sense of the song recommendations.
- What surprised you  
what suprised me is how shifting the genre and energy points awraded changed my list of recommendations. It created wierd outputs like putting a genre that doesnt the user prefrence above one that does but after that the recommendations passed the eye test alot better. I made the neccesary adjustments to the scoring logic though as best as I could without having to add 100 songs.
- Any simple tests or comparisons you ran  
I tried running profiles that seemed paradoxical like; a user who prefer lofi but an intense mood, a rock genre fan whose mood is ambient.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
I would have loved to be able to overhaauled the scoring logic. I would have prefered to use more machine learning concepts for my partial points system but I stayed true to the project suggestions and made the point accumulations based on fixed vaules. 
- Better ways to explain recommendations  
I cant really think of any.
- Improving diversity among the top results  
I'd probably just keep Adjusting the weight each attributes has on a songs final score.
- Handling more complex user tastes  
More complex input handling instead of just using the limited list of mood and genres I stole from spotifys top 20 list as a preset to determining user tastes and how they compare to songs.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
It requires a lot of personal bias. What constitutes what genre a song is in? would someone who loves hard rock like a country song just because it has a similar tempo and acousticness level? Should a song with very similar attributes outside of genre be placed above one with the same genre the user prefered but wildly different attributes? all of these questions are subject to a kind of personal taste thats hard for a programer to decipher from any amount of a users data.
- Something unexpected or interesting you discovered  
Something interesting I discovered is how useful python dictionaries are. They really made all of this alot easier.
- How this changed the way you think about music recommendation apps  
It made me think about how creepy I thought music recommendation apps like spotify were for trying to document every little interaction. I still think how closely they follow every user interaction is strange but now I understand why they place so much importance on a users input history.
