import os
import glob
import re
import numpy as np

# keras
from keras.preprocessing import image
from keras.applications.resnet50 import preprocess_input, decode_predictions
from keras.applications.resnet50 import ResNet50
from keras.models import load_model

# flask
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)


model = ResNet50(weights='imagenet')
print("model load check http://lcoalhost:5000")

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    x = preprocess_input(x)
    preds = model.predict(x)
    return preds



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath,
                                 'uploads',
                                 secure_filename(f.filename))
        f.save(file_path)

        preds = model_predict(file_path, model)

        preds_class = decode_predictions(preds, top=1)
        result = str(preds_class[0][0][1])
        return result
    return None


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
