import streamlit as st
import os
import string
import random
from utils.chatbot import intro_response
from streamlit_theme import st_theme


# Generate a 10 characters ID of pattern:
#   0     1     2     3     4     5     6     7     8     9
# [0-9] [0-9] [A-Z] [A-Z] [A-Z] [0-9] [0-9] [A-Z] [0-9] [A-Z]
def get_survey_id():
    survey_id = ''
    survey_id = survey_id + str(random.randint(0, 9))
    survey_id = survey_id + str(random.randint(0, 9))
    survey_id = survey_id + random.choice(string.ascii_letters)
    survey_id = survey_id + random.choice(string.ascii_letters)
    survey_id = survey_id + random.choice(string.ascii_letters)
    survey_id = survey_id + str(random.randint(0, 9))
    survey_id = survey_id + str(random.randint(0, 9))
    survey_id = survey_id + random.choice(string.ascii_letters)
    survey_id = survey_id + str(random.randint(0, 9))
    survey_id = survey_id + random.choice(string.ascii_letters)
    return survey_id


# Set up the state of this streamlit app session
def session_setup():
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    if 'response_count' not in st.session_state:
        st.session_state['response_count'] = 0

    if 'next_page' not in st.session_state:
        st.session_state.next_page = False

    if 'current_page' not in st.session_state:
        st.session_state.current_page = "chat"

    if 'current_theme' not in st.session_state:
        st.session_state['current_theme'] = st_theme()["base"]

    if 'survey_id' not in st.session_state:
        st.session_state['survey_id'] = get_survey_id()

    if 'survey_finished' not in st.session_state:
        st.session_state['survey_finished'] = False

    if 'submitted_to_database' not in st.session_state:
        st.session_state['submitted_to_database'] = False

    if 'system_instruction' not in st.session_state:
        st.session_state['system_instruction'] = os.getenv("gen_system_instruction")

    if 'introduction' not in st.session_state:
        if os.getenv("intro_system_instruction") == "":
            st.session_state['introduction'] = os.getenv("intro_text")
        else:
            with st.spinner('Launching chatbot, this can take up to 20 seconds...'):
                st.session_state['introduction'] = intro_response()

    if 'next_page' not in st.session_state:
        st.session_state['next_page'] = False

    if 'submitted_input' not in st.session_state:
        st.session_state['submitted_input'] = False

    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = ""


# Save chat history
def modify_chat_history(user_input, response):
    st.session_state['chat_history'].append({
        'user_input': user_input,
        'response': response
    })
