import streamlit as st

st.write('Hello world of streamlit !')

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)