# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented 
    - A: Subgenres are not recgonized ie indie pop wil be overlooked for genre match of pop. This gap reduces accuracy quality. To address this, swap '==' for 'in'
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users 

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
    - A: "High-Energy Pop," "Chill Lofi," and "Deep Intense Rock"

- What you looked for in the recommendations  
    - A: Top 5 reccomendations make sense when compared to ones own musical intuition

- What surprised you 
    - A: Suhbgenre will be missed in origincal "Algorithm Recipie"

- Any simple tests or comparisons you ran  
    - A: Top K returned ie.
        results = rec.recommend(user, k=2)assert len(results) == 2

- For each pair of profiles, write at least one comment comparing the differences between their outputs — what changed, and why does it make sense?
    - A: 
        User 1 prefers high energy
        User 2 prefers a genre with even higher energy
        User 3 profile shifts towards low energy instrumentals

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
    - A: I learned the different types of reccomendations ie context, content, and collaborative

- Something unexpected or interesting you discovered  
    - A: I discovered edge cases and how they impact bot the algorithm design and results ie subgenres "pop: indie pop"

- How this changed the way you think about music recommendation apps  
    - A: This encourages me to 
        think longer on possible edge cases
        continuously iterate so I can experiement/resolve more edge cases
