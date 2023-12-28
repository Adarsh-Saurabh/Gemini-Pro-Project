import os
from flask import Flask, request, render_template
import google.generativeai as genai
from io import BytesIO
from PIL import Image


app = Flask(__name__)

# Set your API key as an environment variable
os.environ['GOOGLE_API_KEY'] = "AIzaSyDZdasVyl4z3u0VvBi0qQbuUqxnN0I4iYI"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro-vision')

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/generate', methods=['POST'])
# def generate():
#     try:
#         user_input = request.form['user_input']
#         image_input = request.files['image_upload']

#         if image_input:
#             # Assuming you want to use both user input and the uploaded image
#             response_content = model.generate_content([image_input, user_input], stream=True)
#             generated_text = response_content.text
#             print("nice")
#         else:
#             generated_text = "Error: No image uploaded."

#     except Exception as e:
#         generated_text = f"Error: {str(e)}"

#     return render_template('index.html', generated_text=generated_text)


@app.route('/', methods=['POST'])
def generate():
    try:
        user_input = request.form['user_input']

        # Check if 'image_upload' is in request.files
        if 'image_upload' in request.files:
            image_input = request.files['image_upload']

            # Convert FileStorage to PIL Image
            image_data = BytesIO(image_input.read())
            image = Image.open(image_data)

            response_content = model.generate_content([user_input, image], stream=True)
            
            # Resolve the response before accessing its attributes
            response_content.resolve()

            generated_text = response_content.text
            print("nice")
        else:
            generated_text = "Error: No image uploaded."

    except Exception as e:
        generated_text = f"Error: {str(e)}"
    print(generated_text)
    return render_template('index.html', generated_text=generated_text)

# if __name__ == '__main__':
#     app.run(debug=True)
