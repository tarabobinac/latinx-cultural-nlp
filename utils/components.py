import streamlit as st
from utils.chatbot import get_response
from utils.session import modify_chat_history
from streamlit_theme import st_theme


minimum_responses = 5
warning_responses = 10
maximum_responses = 15


def show_response_count():
    response_count = st.session_state['response_count']

    if response_count == 0:
        return

    response_count_message = "You have finished {} round(s) of conversation.".format(
        response_count)

    # Need more responses
    if response_count < warning_responses:
        st.info(response_count_message)

    # Enough but can ask more
    if warning_responses <= response_count < maximum_responses:
        extra_count = maximum_responses - response_count
        response_count_message += ' Due to time limit, you can only ask {} more question to the chatbot.'.format(
            extra_count)
        st.warning(response_count_message)

    # Done
    if maximum_responses <= response_count:
        st.success(response_count_message)


def finish_button():
    response_count = st.session_state['response_count']

    if st.session_state['survey_finished']:
        st.button('Finish Chat', disabled=True)
        return

    if response_count == maximum_responses:
        st.session_state['survey_finished'] = True

    if response_count >= minimum_responses:
        if st.button('Finish Chat'):
            st.session_state['survey_finished'] = True
            st.rerun()


def done_button():
    if st.session_state['survey_finished']:
        if st.button('Submit', disabled=st.session_state.get('done_pressed', False)):
            st.session_state['done_pressed'] = True
            st.rerun()


def show_finish_status():

    if not st.session_state['survey_finished']:
        return

    if st.session_state['next_page']:
        st.button('Next page', disabled=True)
        return

    st.success(f'''
      **Chat complete**, thank you for chatting with the chatbot!\n
      Sometimes, chatbots produce responses that are inaccurate in a few different ways. Press 
      **Next page** to review the chatbot's responses from this chat and provide feedback on them.
    ''')

    if st.button("Next page"):
        st.session_state["next_page"] = True
        st.rerun()


def add_reaction_buttons(response_index):
    emojis = ["👍", "👎", "❤️", "😂", "😮", "😢", "😡"]

    # Check if it's the latest response
    is_latest_response = (response_index == len(st.session_state['chat_history']) - 1)

    # Disable reaction buttons for previous responses, enable only for the latest response
    disabled = not is_latest_response

    selected_emoji = st.radio(
        f"React to response {response_index + 1}:",
        emojis,
        key=f"reaction_{response_index}",
        index=None,  # No default selection
        horizontal=True,
        disabled=disabled
    )

    # Initialize reaction history if not already
    if 'reaction_history' not in st.session_state:
        st.session_state['reaction_history'] = []

    # Add selected emoji to the history or update it
    if len(st.session_state['reaction_history']) == response_index:
        st.session_state['reaction_history'].append(selected_emoji)
    elif st.session_state['reaction_history'][response_index] != selected_emoji:
        st.session_state['reaction_history'][response_index] = selected_emoji

    # If it's the latest response, ensure that the user selects an emoji
    if is_latest_response and selected_emoji is None:
        st.warning(f"Please select an emoji reaction for response {response_index + 1} to proceed.")
        st.stop()


def comments():
    feedback_enabled_count = 0  # Track how many responses have feedback enabled
    valid_comments_count = 0    # Track how many valid comments (with categories) have been provided

    if st.session_state['current_theme'] == "dark":
        background_color_user = "#5f6759"
        background_color_bot = "#434343"
    else:
        background_color_user = "#dcf8c6"
        background_color_bot = "#f1f0f0"

    # Initialize session state for 'done_pressed' if not already done
    if 'done_pressed' not in st.session_state:
        st.session_state['done_pressed'] = False

    # Process the responses
    for i, exchange in enumerate(st.session_state.get('chat_history', [])):
        st.markdown(f"<h5><b>Response {i + 1}</b></h5>", unsafe_allow_html=True)

        # Create columns for layout
        col1, col2 = st.columns([3, 2])

        with col1:
            # Add the user's input in a separate colored box above the model's response
            st.markdown(f"""
                <div style='background-color: {background_color_user}; padding: 10px; border-radius: 10px; margin-bottom: 10px;'>
                    <strong>User:</strong> {exchange['user_input']}
                </div>
            """, unsafe_allow_html=True)

            # Add the model's response in a text box below the user's input
            st.markdown(f"""
                <div style='background-color: {background_color_bot}; padding: 10px; border-radius: 15px; margin-bottom: 10px;
                min-height: 243px; display: block;'>
                    <strong>Response:</strong> {exchange['response']}
                </div>
            """, unsafe_allow_html=True)

        with col2:
            # Disable buttons and inputs if submit has been pressed
            feedback_option = st.radio("Give feedback?", ["No", "Yes"], index=0, key=f"feedback_{i}",
                                       horizontal=True, disabled=st.session_state['done_pressed'])

            if feedback_option == "Yes":
                feedback_enabled_count += 1

            categories = st.multiselect(
                f"Categories for Response {i + 1}",
                ["Balanced / biased towards certain perspective",
                 "Morally + ethically sound / morally + ethically questionable", "Factually incorrect",
                 "Respectful / disrespectful", "Culturally relevant / culturally irrelevant", "Other"],
                key=f"categories_{i}",
                disabled=feedback_option != "Yes" or st.session_state['done_pressed']
            )

            # Comment text box for feedback
            comment = st.text_area(f"Comment for Response {i + 1}", key=f'comment_{i}',
                                   disabled=feedback_option != "Yes" or st.session_state['done_pressed'],
                                   placeholder="Add your comment here")

            # Check if a valid comment and category selection are provided for this response
            if feedback_option == "Yes" and comment.strip() and categories:
                valid_comments_count += 1

    # Enforce at least two responses with valid feedback (comment and category) enabled
    submit_button_disabled = valid_comments_count < 2

    if st.session_state['survey_finished'] and not submit_button_disabled:
        if st.button('Submit', disabled=st.session_state.get('done_pressed', False)):
            st.session_state['done_pressed'] = True
            st.rerun()



def submit_user_input():
    if st.session_state['survey_finished']:
        st.text_input('You:', value='', key=str(st.session_state['response_count']), disabled=True)
        return None
    else:
        return st.text_input('You:', value='', key=str(st.session_state['response_count']))

def get_input_and_gen_response():
    if not st.session_state['submitted_input']:
        user_input = submit_user_input()
        if user_input:
            st.session_state['user_input'] = user_input
            st.session_state['submitted_input'] = True
            st.rerun()

    else:
        st.markdown(f"""
            <div class="chat-container">
                <div class="user-message">{st.session_state['user_input']}</div>
            </div>
        """, unsafe_allow_html=True)
        response = get_response(st.session_state['user_input'])
        st.session_state['submitted_input'] = False
        if response:
            modify_chat_history(st.session_state['user_input'], response)
            st.session_state['response_count'] += 1
            st.rerun()