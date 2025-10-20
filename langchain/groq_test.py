from groq import Groq
import os
from utils import get_completion
from dotenv import load_dotenv
load_dotenv()      # reads local .env file


# # 1. Basic Groq API flow
# print(get_completion("What 1+1?"))


# Customizing a Prompt to have appropriate language

customer_email = """
Arrr, I be fuming that my blender lid flew off and splattered me kitchen walls with smoothie! \
And to make matters worst, the warranty dont cover the cost of cleaning up me kitchen. I need your help rignt now. mate!
"""

style = """Cyrillic Russian, in a calm and respectful tone"""

prompt = f""" Translate the text that is delimited by triple backticks into a style that is {style}.
text: ```{customer_email}```
"""

print(prompt)
print(get_completion(prompt=prompt))