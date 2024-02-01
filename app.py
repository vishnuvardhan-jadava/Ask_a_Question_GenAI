import streamlit as st
import google.generativeai as genai

API_KEY = 'AIzaSyBsTUgZ2q2WPJyxtDF_9lDmkzhwPXlwPvE'

genai.configure(api_key=API_KEY)

st.set_page_config(page_title='Q and A with Google Gemini-Pro')
st.header('Enter your question')
user_input = st.text_input(label='Ask gemini pro any question(no history chat history is maintained)', label_visibility='hidden',placeholder='enter text')
submit = st.button('Ask')
model = genai.GenerativeModel('gemini-pro')
if user_input and submit:
    response = model.generate_content(user_input)
    st.header('Response')
    st.write(response.text)