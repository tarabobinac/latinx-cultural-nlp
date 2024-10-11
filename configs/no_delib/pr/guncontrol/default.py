# config.py

import os
import subprocess

# Setting environment variables
os.environ['topic'] = 'o controle de armas'

os.environ['intro_temp'] = '0.7'
os.environ['intro_top_p'] = '0.9'
os.environ['intro_rep_pen'] = '1'
os.environ['intro_max_tokens'] = '512'

os.environ['intro_system_instruction'] = ''
os.environ['intro_text'] = f"""Vamos falar sobre {os.environ['topic']}! Comece nos contando algo que te confunde sobre {os.environ['topic']}."""


os.environ['gen_temp'] = '0.7'
os.environ['gen_top_p'] = '0.9'
os.environ['gen_rep_pen'] = '1'
os.environ['gen_max_tokens'] = '512'
os.environ['gen_system_instruction'] = f"Termine a sua resposta dentro de {os.environ['gen_max_tokens']} tokens."

# Run the Streamlit app
subprocess.run(["streamlit", "run", "./app.py"])
