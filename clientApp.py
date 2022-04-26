from flask import Flask, request, jsonify
import os
from flask_cors import CORS, cross_origin
from utils import decodeImage
from predict import ocr

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.objectDetection = ocr(self.filename)


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.objectDetection.getPrediction()
    return jsonify({"result" : result})

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host='127.0.0.1', port=7000, debug=True)