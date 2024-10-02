# config.sh

export intro_temp=0.7
export intro_top_p=0.9
export intro_rep_pen=1
export intro_max_tokens=512
export intro_system_instruction="Respond with a list of pros and cons on the topic at hand."
export intro_text="""Imagine you are a person from the United States moderating a discussion about gun control. Based on
                the cultural values from the United States, provide your communication partner with stances why an average
                person from the United States would be pro/against gun control. You should provide information in a casual
                style in English. Start the conversation with exactly the following prompt and the culturally-relevant
                information:\n\n\"Good afternoon. I will be your conversation partner today in a brief discussion about gun
                control. This discussion is an opportunity for you to learn about gun control. I want to encourage you to speak
                freely. You are not expected to be an expert. Also, no consensus is necessary, you do not need to agree with
                the stances I provide. My role is to facilitate your understanding of gun control across cultural viewpoints.
                Please start off by telling us something that puzzles you about this topic.\""""

export gen_temp=0.7
export gen_top_p=0.9
export gen_rep_pen=1
export gen_max_tokens=512
export gen_system_instruction="You finish your response within ${gen_max_tokens} tokens."

streamlit run ./info-gun-control.py