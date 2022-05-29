# Content-Based-Movie-Recommender-System
Content Based Recommender System recommends movies similar to the movie selected by user and recommends movies based on cosine similarity with other movies.

![Python](https://img.shields.io/badge/Python-3.9-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![API](https://img.shields.io/badge/API-TMDB-fcba03) 
 
## Introduction
Developed an intelligent application that recommends user movies related to the movie selected by the them based on `Cosine Similarity` among the movies.

## 🧾 Dataset: 
The dataset is based on TMDB movies dataset with record of about 5000 movies.
##### Sources of the datasets 

1. [IMDB 5000 Movie Dataset](https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset)
2. [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset)
3. [List of movies in 2018](https://en.wikipedia.org/wiki/List_of_American_films_of_2018)
4. [List of movies in 2019](https://en.wikipedia.org/wiki/List_of_American_films_of_2019)
5. [List of movies in 2020](https://en.wikipedia.org/wiki/List_of_American_films_of_2020)

## :bar_chart: Exploratory Data Analysis:
* Exploratory Data Analysis is the first step of understanding your data and acquiring domain knowledge. 

### :hourglass: Data Preprocessing:
#### 1.) Data Preprocessing:
 At first, the dataset is cleaned where:
 * Converted genre, keywords and cast as a list of strings where for cast we have selected top 3 casts for each movie.
 * For the crew column, I have selected only director's name.
 * After data cleaning, I combined overview, cast, keywords, casts and crew columns into a single column tags.

#### 2.) Vectorization:
 * I have used **Bag of Words** to tokenize the input sequences. I have used CountVectorizer for this.

#### 3.) Cosine Similarity:
 * I calculated cosine similarity among each vectors and stored them as a matrix `similarity`.

##### Similarity Score:
 How does it decide which item is most similar to the item user likes? Here come the similarity scores.
 It is a numerical value ranges between zero to one which helps to determine how much two items are similar to each other on a scale of zero to one. This similarity   score is obtained measuring the similarity between the text details of both of the items. So, similarity score is the measure of similarity between given text       details of two items. This can be done by cosine-similarity.
   
##### How Cosine Similarity works?
 Cosine similarity is a metric used to measure how similar the documents are irrespective of their size. Mathematically, it measures the cosine of the angle between   two vectors projected in a multi-dimensional space. The cosine similarity is advantageous because even if the two similar documents are far apart by the Euclidean   distance (due to the size of the document), chances are they may still be oriented closer together. The smaller the angle, higher the cosine similarity.
  
  ![image](https://user-images.githubusercontent.com/36665975/70401457-a7530680-1a55-11ea-9158-97d4e8515ca4.png)
  > More about Cosine Similarity : [Understanding the Math behind Cosine Similarity](https://www.machinelearningplus.com/nlp/cosine-similarity/)

## Making Recommendations:
* Based on the movie name given by user, it's similarity score is extracted from the `similarity matrix`.
* The similarity scores are sorted in descending order and top 5 movies are selected.

```
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_preference = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_preference.append(i[1])
```

## Web Application :computer: :earth_americas: :
* Built a web application using **Streamlit** and deployed on **streamlit-cloud**.

> #### Link to "**Movie Recommender System**" application: https://the-movie-buff.herokuapp.com/

