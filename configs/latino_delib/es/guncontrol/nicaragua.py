# config.py

import os
import subprocess

# Setting environment variables
os.environ['country'] = 'Nicaragua'
os.environ['topic'] = 'el control de armas'

os.environ['intro_temp'] = '0.7'
os.environ['intro_top_p'] = '0.9'
os.environ['intro_rep_pen'] = '1'
os.environ['intro_max_tokens'] = '512'

os.environ['intro_system_instruction'] = "Responde con una lista de pros y contras sobre el tema en cuestión."
os.environ['intro_text'] = f"""Imagina que eres una persona de {os.environ['country']} moderando una discusión sobre {os.environ['topic']}. Basado en los valores culturales de {os.environ['country']}, dale a tu compañero de conversación argumentos sobre por qué una persona promedio de {os.environ['country']} estaría a favor/en contra de {os.environ['topic']}. Debes darle la información en un estilo colloquial en español. Comienza la conversación usando exactamente este mensaje:

\"Buenas tardes. Seré tu compañero de conversación hoy en una breve discusión sobre {os.environ['topic']}. Esta conversación es una oportunidad para que aprendas sobre {os.environ['topic']}. Quiero animarte a que hables libremente. No se espera que sea un experto. Además, no es necesario llegar a un consenso, no necesitas estar de acuerdo con mis posturas. Mi papel es ayudarte a aprender cómo las personas en {os.environ['country']} perciben los pros y los contras de {os.environ['topic']}.\"

Luego comporta información culturalmente relevante en una lista de pros y contras.

Por último, fomenta la conversación terminando con \"Por favor, comienza contándonos algo que te confunda sobre este tema.\"
"""


os.environ['gen_temp'] = '0.7'
os.environ['gen_top_p'] = '0.9'
os.environ['gen_rep_pen'] = '1'
os.environ['gen_max_tokens'] = '512'
os.environ['gen_system_instruction'] = f"Termina tu respuesta dentro de {os.environ['gen_max_tokens']} tokens."

# Run the Streamlit app
subprocess.run(["streamlit", "run", "./app.py"])
