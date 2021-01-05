# Flask for web app
import flask as fl
from flask import jsonify, request
#keras model 
import keras.models
from keras.models import load_model 
#tensorflow
import tensorflow as tf
#numpy
import numpy as np

#create a new web app
app = fl.Flask(__name__)

model = load_model('model1.h5')

#add a root route.
@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/api/power')
def random():
    return{"value": np.random.normal()}
#Copied and adapted from https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
# define a predict function as an endpoint 
@app.route("/api/predict", methods=["GET","POST"])
def predict():
    if request.method == "GET":
        result = request.form.get('speed')
        data = model.predict([7])
        x = data.tolist()
        # return a response in json format 
        return jsonify({"value": x})
    else:
        return ("index.html")