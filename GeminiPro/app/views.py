from django.shortcuts import render
from django.http import HttpResponse
import os
from flask import Flask, request, render_template
import google.generativeai as genai
from django.views.decorators.csrf import csrf_protect
import pyttsx3

app = Flask(__name__)
# Set your API key as an environment variable
os.environ['GOOGLE_API_KEY'] = "AIzaSyDZdasVyl4z3u0VvBi0qQbuUqxnN0I4iYI"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')


# Create your views here.
def page(request):
    return render(request, 'index.html')
    # return HttpResponse("hi how are you!")




# def generate(request):
#     if request.method == 'POST':  # Handle only POST requests
#         user_input = request.POST.get('user_input')  # Access form data correctly
#         try:
#             response = model.generate_content(user_input)
#             generated_text = response.text
#             print("Successfull!")
#         except Exception as e:
#             generated_text = f"Error: {str(e)}"
#         return render(request, 'index.html', {'generated_text': generated_text})
@csrf_protect
def generate(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = model.generate_content(user_input)  # Replace with your AI model's generation call
        generated_text = response.text

        # Text-to-speech using pyttsx3
        engine = pyttsx3.init()
        engine.save_to_file(generated_text, 'static/output.mp3')
        engine.runAndWait()

        return render(request, 'index.html', {'generated_text': generated_text, 'audio_file_path': '/static/output.mp3'})

    else:
        return render(request, 'index.html')




if __name__ == '__main__':
    app.run(debug=True)