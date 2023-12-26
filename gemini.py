import os
import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
# from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.environ['GOOGLE_API_KEY'] = "AIzaSyDZdasVyl4z3u0VvBi0qQbuUqxnN0I4iYI"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

inpp = input("Write")

response = model.generate_content(inpp)
print(response.text)

# print(response.prompt_feedback)

# for chunk in response:
#   print(chunk.text)
#   print("_"*80)


# response = model.generate_content("What is the meaning of life?", stream=True)