import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movie_indices:
        movie_id = movies_df.iloc[i[0]].movie_id
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies


movies_df = pickle.load(open('movies.pkl', 'rb'))
movies = movies_df['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))



st.markdown("<h1 style='color: red;' 'align-items: center' >Lets select your Movie!</h1>", unsafe_allow_html=True)

selected_movie_name = st.selectbox('Drop your favorite', movies)

if st.button('Btao bhayy'):
    names = recommend(selected_movie_name)
    st.markdown("<h4 style='color: blue;' 'align-items: center' >Lets select your Movie!</h1>", unsafe_allow_html=True)
    for i in range(5):
        st.text(f"{i+1}. {names[i]}")
    
   
    st.markdown(
    """
  
    
    <style>
   
    .title {
        font-size:90px;
        color: #FF6347; 
        text-align: center;
        font-weight: bold;
    }
    .bhay{
        height = 100%
        width = 100%    
            }
    .bg{
         display: block; 
         width: 10% !important; 
         height: 10vh !important; 
         object-fit: cover; 
         position: absolute; 
         top: 0; 
         left: 0; 
         z-index: -1;
    }
    body {
        background-image: url('https:
    
    

    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="title">Happy Streaming!</p>'
            , unsafe_allow_html=True)



