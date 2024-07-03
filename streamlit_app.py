import streamlit as st
import requests

# Function to call the Finnish Tarot Card API
def get_tarot_reading(user_question, conversation_id):
    url = f"https://lobster-app-e45d3.ondigitalocean.app/question?user_question={user_question}&conversation_id={conversation_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to get a response from the API.")
        return None

# Streamlit App
st.title("Finnish Tarot Cards API")
st.write("This app communicates with a Finnish Tarot Card API to provide a tarot reading based on your question.")

st.header("How to use this API")
st.write("""
1. Enter your question in the text box provided.
2. Enter a conversation ID to track your session.
3. Click on 'Get Reading' to receive your tarot card reading.

**API Documentation:**
- **Endpoint:** `https://lobster-app-e45d3.ondigitalocean.app/question`
- **Method:** GET
- **Payload:**
    - `user_question` (string): The question you want to ask.
    - `conversation_id` (integer): A unique identifier for your session.
- **Response:**
    - `conversation_id` (integer): The conversation ID you provided.
    - `card_list` (list): A list of 3 card names.
    - `reading` (string): The tarot card reading based on your question.
""")

st.header("Use the API")

# Input fields
user_question = st.text_input("Enter your question:", placeholder="What does the future hold for me?")
conversation_id = st.number_input("Enter a conversation ID:", min_value=0, value=0, step=1)

if st.button("Get Reading"):
    if user_question and conversation_id:
        result = get_tarot_reading(user_question, conversation_id)
        if result:
            st.subheader("Tarot Reading Result")
            st.json(result)
    else:
        st.error("Please enter both your question and conversation ID.")
