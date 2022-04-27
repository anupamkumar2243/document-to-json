from flask import Flask, request, jsonify,render_template
import os
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from utils import decodeImage
from predict import ocr
import json
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

UPLOAD_FOLDER = 'static/uploads/'

ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','txt','pdf'])

app = Flask(__name__)
CORS(app)

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

"""class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.objectDetection = ocr(self.filename)"""

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/upload', methods=['GET','POST'])


def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', msg= 'No file selected')
        file = request.files['file']

        if file.filename =='':
            return render_template('index.html', msg='No file selected')
        if file and allowed_file(file.filename):
            extracted_file = ocr(file)
            return render_template('index.html',
            msg='Successfully processed',
            extracted_file=extracted_file,
            img_src=UPLOAD_FOLDER + file.filename)
    elif request.method =='GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run()








'''@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.objectDetection.getPrediction()
    return jsonify({"result" : result})

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='127.0.0.1', port=7000, debug=True)'''
