# config.py

import os
import subprocess

# Setting environment variables
os.environ['country'] = 'the United States'
os.environ['topic'] = 'abortion'

os.environ['intro_temp'] = '0.7'
os.environ['intro_top_p'] = '0.9'
os.environ['intro_rep_pen'] = '1'
os.environ['intro_max_tokens'] = '512'

os.environ['intro_system_instruction'] = "Respond with a list of pros and cons on the topic at hand."
os.environ['intro_text'] = f"""Imagine you are a person from {os.environ['country']} moderating a discussion about {os.environ['topic']}. Based on the cultural values from {os.environ['country']}], provide your communication partner with stances why an average person from {os.environ['country']} would be pro/against {os.environ['topic']}. You should provide information in a casual style in English. Start the conversation with exactly the following prompt: 

\"Good afternoon. I will be your conversation partner today in a brief discussion about {os.environ['topic']}. This discussion is an opportunity for you to learn about {os.environ['topic']}. I want to encourage you to speak freely. You are not expected to be an expert. Also, no consensus is necessary, you do not need to agree with the stances I provide. My role is to help you learn about how people in {os.environ['country']} perceive the pros and cons of {os.environ['topic']}.\"

And then provide relevant cultural information in a pros/cons list. 

Lastly, encourage conversation by ending with \"Please start off by telling us something that puzzles you about this topic.\"
"""

os.environ['gen_temp'] = '0.7'
os.environ['gen_top_p'] = '0.9'
os.environ['gen_rep_pen'] = '1'
os.environ['gen_max_tokens'] = '512'
os.environ['gen_system_instruction'] = f"You finish your response within {os.environ['gen_max_tokens']} tokens."

# Run the Streamlit app
subprocess.run(["streamlit", "run", "./app.py"])
