import streamlit as st

st.title('My first STREAMLIT app')
st.header('This Streamlit framework is used for Web App')
st.sidebar("Sidebar of Streamlit app")
st.markdown('This is markdown using Streamlit')
choices = [25, 50, 75, 100]
st.slider([choices])