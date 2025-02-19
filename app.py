import streamlit as st 
import pickle
import pandas as pd 
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0d425f3a49f8723298d9abd7b6f732a8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    

# Recommend function ( it will recommend the movies)
def recommend(movie_name):
    if movie_name not in movies['title'].values:
        return ["Movie not found."]
    movie_index = movies[movies['title'] == movie_name].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies , recommended_movies_posters

# Load movies and similarity data (it will load and finds the similarity between movies)
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI (it creates the frontend of the website)
st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    'Which movie do you want to watch?',
    movies_list
)

if st.button('Recommend'):
    names , posters = recommend(selected_movie_name)
    col1, col2, col3 ,col4 ,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
