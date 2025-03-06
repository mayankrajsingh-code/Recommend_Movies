import pandas as pd
import streamlit as st
import pickle
import requests

def fetch_poster (title):
    API_KEY = "1d2682c8"
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["Poster"]


def rec(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = cs[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        title=movies.iloc[i[0]].title
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(title))
    return recommended_movies, recommended_movies_posters

#All pickle files
movies_dict=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
cs=pickle.load(open('cosim.pkl','rb'))

#Header
st.title('Movie Recommender System')

#A selectbox to select the movies and get them store in smn variable
#title column from the movies dataframe that derived from movies_dict pickle file
smn = st.selectbox(
    "Movie Search",
    movies['title'].values)


if st.button("Recommend"):
    names,posters=rec(smn)

    col1, col2, col3, col4, col5 = st.columns(5)

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
