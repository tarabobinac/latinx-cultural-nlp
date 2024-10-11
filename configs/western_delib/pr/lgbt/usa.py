# config.py

import os
import subprocess

# Setting environment variables
os.environ['country'] = 'o Estados Unidos'
os.environ['topic'] = 'os direitos LGBTQ'

os.environ['intro_temp'] = '0.7'
os.environ['intro_top_p'] = '0.9'
os.environ['intro_rep_pen'] = '1'
os.environ['intro_max_tokens'] = '512'

os.environ['intro_system_instruction'] = "Responda com uma lista de prós e contras sobre o tema em questão."
os.environ['intro_text'] = f"""Imagine que você é uma pessoa do {os.environ['country']} moderando uma discussão sobre {os.environ['topic']}]. Com base nos valores culturais do {os.environ['country']}, forneça ao seu companheiro de comunicação argumentos sobre por que uma pessoa média do {os.environ['country']} estaria a favor ou contra {os.environ['topic']}. Você deve fornecer informações em um estilo casual em português. Comece a conversa exatamente com o seguinte aviso:


\"Boa tarde. Serei seu companheiro de conversa hoje em uma breve discussão sobre {os.environ['topic']}. Esta discussão é uma oportunidade para você aprender sobre {os.environ['topic']}. Quero encorajá-lo a falar livremente. Não se espera que você seja um especialista. Além disso, não é necessário chegar a um consenso, você não precisa concordar com as posturas que eu fornecer. Meu papel é te ajudar a aprender como as pessoas no Brasil percebem os prós e os contras de {os.environ['topic']}.\"


E então forneça informações culturalmente relevantes em uma lista de prós e contras.


Por último, incentive a conversa terminando com \"Por favor, comece nos contando algo que te confunde sobre este tema.\"
"""



os.environ['gen_temp'] = '0.7'
os.environ['gen_top_p'] = '0.9'
os.environ['gen_rep_pen'] = '1'
os.environ['gen_max_tokens'] = '512'
os.environ['gen_system_instruction'] = f"Termine a sua resposta dentro de {os.environ['gen_max_tokens']} tokens."

# Run the Streamlit app
subprocess.run(["streamlit", "run", "./app.py"])
