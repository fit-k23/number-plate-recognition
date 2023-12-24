from flask import Flask, render_template, request
import os
from flask.templating import render_template
from flask import Flask
from flask_ngrok import run_with_ngrok
from model import OCR
# webserver gateway interface

template_folder = '/content/drive/MyDrive/npr/WebbApp/templates'

app = Flask (__name__,template_folder=template_folder)
run_with_ngrok(app)
BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(
    BASE_PATH, '/content/drive/MyDrive/npr/WebbApp/static/upload')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH, filename)
        upload_file.save(path_save)
        text = OCR(path_save, filename)

        return render_template('index.html', upload=True, upload_image=filename, text=text)

    return render_template('index.html', upload=False)


if __name__ == "__main__":
    app.run()