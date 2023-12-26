import os
from flask import Flask, request, render_template
import google.generativeai as genai
import pyttsx3

app = Flask(__name__)

# Set your API key as an environment variable
os.environ['GOOGLE_API_KEY'] = "AIzaSyDZdasVyl4z3u0VvBi0qQbuUqxnN0I4iYI"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']

    try:
        response = model.generate_content(user_input)
        generated_text = response.text
        print("nice")

        # Text-to-speech using pyttsx3
        engine = pyttsx3.init()
        engine.save_to_file(generated_text, 'static/output.mp3')
        engine.runAndWait()

    except Exception as e:
        generated_text = f"Error: {str(e)}"

    return render_template('index.html', generated_text=generated_text, audio_file_path='/static/output.mp3')

if __name__ == '__main__':
    app.run(debug=True)
