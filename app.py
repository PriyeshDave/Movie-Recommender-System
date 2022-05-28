import pickle
import streamlit as st
import requests
from PIL import Image
from zipfile import ZipFile

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

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

    return recommended_movie_names,recommended_movie_posters, recommended_movie_preference


st.set_page_config(page_title="Movies Recommender System",
                   page_icon="🎥", layout="wide")

# creating a side bar 
sidebar_image = Image.open('side banner.jpg')
st.sidebar.info("Created By : Priyesh Dave")
# Adding an image to the side bar 
st.sidebar.image(sidebar_image, width=None)
st.sidebar.subheader("Contact Information : ")
col1, mid, col2 = st.columns([1,1,20])
with col1:
	st.sidebar.subheader("LinkedIn : ")
with col2:
	st.sidebar.markdown("[![Linkedin](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLsu_X_ZxDhuVzjTHvk4eZOmUDklreUExhlw&usqp=CAU)](https://www.linkedin.com/in/priyeshdave21/)")

col3, mid, col4 = st.columns([1,1,20])
with col3:
	st.sidebar.subheader("Github : ")
with col4:
	st.sidebar.markdown("[![Github](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJGtP-Pq0P67Ptyv3tB7Zn2ZYPIT-lPGI7AA&usqp=CAU)](https://github.com/PriyeshDave)")

#creating option list for dropdown menu
st.markdown("<h1 style='text-align: center;'>Movies Recommender System </h1>", unsafe_allow_html=True)
banner = Image.open('banner_mrs.png')
st.image(banner)

movies = pickle.load(open('./Models/movie_list.pkl','rb'))
with ZipFile('./Models/similarity.zip', 'r') as zipObj:
   # Extract all the contents of zip file in current directory
   zipObj.extractall('./Models/similarity.pkl')

similarity = pickle.load(open('./Models/similarity.pkl/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):

    st.markdown("<h2 style='text-align: center;'>YOU MIGHT LIKE </h2>", unsafe_allow_html=True)
    st.markdown(" ", unsafe_allow_html=True)
    st.markdown(" ", unsafe_allow_html=True)
    st.markdown(" ", unsafe_allow_html=True)

    recommended_movie_names,recommended_movie_posters, recommended_movie_preference= recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        similarity = round(recommended_movie_preference[0], 2)
        if(similarity >= .45):
            st.markdown("⭐⭐⭐⭐⭐")
        elif(similarity >= .40 and similarity < .45):
            st.markdown("⭐⭐⭐⭐")
        elif(similarity >= .30 and similarity < .40):
            st.markdown("⭐⭐⭐")
        elif(similarity >= .20 and similarity < .30):
            st.markdown("⭐⭐")    
        else:
            st.markdown("⭐")

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        similarity = round(recommended_movie_preference[1], 2)
        if(similarity >= .45):
            st.markdown("⭐⭐⭐⭐⭐")
        elif(similarity >= .40 and similarity < .45):
            st.markdown("⭐⭐⭐⭐")
        elif(similarity >= .30 and similarity < .40):
            st.markdown("⭐⭐⭐")
        elif(similarity >= .20 and similarity < .30):
            st.markdown("⭐⭐")    
        else:
            st.markdown("⭐")

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        similarity = round(recommended_movie_preference[2], 2)
        if(similarity >= .45):
            st.markdown("⭐⭐⭐⭐⭐")
        elif(similarity >= .40 and similarity < .45):
            st.markdown("⭐⭐⭐⭐")
        elif(similarity >= .30 and similarity < .40):
            st.markdown("⭐⭐⭐")
        elif(similarity >= .20 and similarity < .30):
            st.markdown("⭐⭐")    
        else:
            st.markdown("⭐")

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        similarity = round(recommended_movie_preference[3], 2)
        if(similarity >= .45):
            st.markdown("⭐⭐⭐⭐⭐")
        elif(similarity >= .40 and similarity < .45):
            st.markdown("⭐⭐⭐⭐")
        elif(similarity >= .30 and similarity < .40):
            st.markdown("⭐⭐⭐")
        elif(similarity >= .20 and similarity < .30):
            st.markdown("⭐⭐")    
        else:
            st.markdown("⭐")

    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        similarity = round(recommended_movie_preference[4], 2)
        if(similarity >= .45):
            st.markdown("⭐⭐⭐⭐⭐")
        elif(similarity >= .40 and similarity < .45):
            st.markdown("⭐⭐⭐⭐")
        elif(similarity >= .30 and similarity < .40):
            st.markdown("⭐⭐⭐")
        elif(similarity >= .20 and similarity < .30):
            st.markdown("⭐⭐")    
        else:
            st.markdown("⭐")





