# config.py

import os
import subprocess

# Setting environment variables
os.environ['topic'] = 'abortion'

os.environ['intro_temp'] = '0.7'
os.environ['intro_top_p'] = '0.9'
os.environ['intro_rep_pen'] = '1'
os.environ['intro_max_tokens'] = '512'

os.environ['intro_system_instruction'] = ''
os.environ['intro_text'] = f"""Let\'s talk about {os.environ['topic']}! Start off by telling me something that puzzles you about {os.environ['topic']}."""


os.environ['gen_temp'] = '0.7'
os.environ['gen_top_p'] = '0.9'
os.environ['gen_rep_pen'] = '1'
os.environ['gen_max_tokens'] = '512'
os.environ['gen_system_instruction'] = f"You finish your response within {os.environ['gen_max_tokens']} tokens."

# Run the Streamlit app
subprocess.run(["streamlit", "run", "./app.py"])
