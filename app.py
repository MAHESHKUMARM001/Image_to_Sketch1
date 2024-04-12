# from flask import Flask, render_template, request
# import cv2
# import numpy as np

# app = Flask(__name__, template_folder="templates")


# def pencil_sketch(image):
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#     inverted_image = 255 - gray_image
#     blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
#     inverted_blurred = 255 - blurred
#     pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
#     return pencil_sketch

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     if 'file' not in request.files:
#         return render_template('index.html', message='No file part')
    
#     file = request.files['file']
#     if file.filename == '':
#         return render_template('index.html', message='No selected file')

#     if file:
#         # Read image
#         nparr = np.fromstring(file.read(), np.uint8)
#         image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
#         # Process image
#         sketch = pencil_sketch(image)
        
#         # Save processed image
#         cv2.imwrite("static/pencil_sketch.jpg", sketch)
        
#         return render_template('index.html', message='Image uploaded successfully',
#                                sketch='static/pencil_sketch.jpg', image='static/original.jpg')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request
import cv2
import numpy as np
import os

app = Flask(__name__, template_folder="templates")

def pencil_sketch(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    return pencil_sketch

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('index.html', message='No file part')

    file = request.files['file']
    if file.filename == '':
        return render_template('index.html', message='No selected file')

    if file:
        # Read image
        nparr = np.fromstring(file.read(), np.uint8)
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Process image
        sketch = pencil_sketch(image)

        # Save processed image
        sketch_path = "static/pencil_sketch.jpg"
        original_path = "static/original.jpg"
        cv2.imwrite(sketch_path, sketch)
        cv2.imwrite(original_path, image)

        return render_template('index.html', message='Image uploaded successfully',
                               sketch=sketch_path, image=original_path)

if __name__ == '__main__':
    app.run(debug=True)
