# Flask for web app
import flask as fl
from flask import jsonify, request, json
import requests
#tensorflow
import tensorflow
import keras
#keras 
from keras.models import load_model 
#numpy
import numpy as np

#create a new web app
app = fl.Flask(__name__)

model = load_model('model1.h5')

#add a root route.
@app.route('/', methods=["GET","POST"])
def home():
    return app.send_static_file('index.html')

@app.route('/api/power')
def random():
    return{"value": np.random.normal()}
#Copied and adapted from https://towardsdatascience.com/deploying-keras-deep-learning-models-with-flask-5da4181436a2
# define a predict function as an endpoint 
@app.route('/api/predict', methods=["GET","POST"])
def predict():
        #json_data = request.get_json(force=True)
        #value = json_data["inputspd"]
        result12 = 12
        #print(type(json_data))      
        print(result12)
        #print(json_data)
        data = model.predict([result12])
        x = data.tolist()
        # return a response in json format  
        return jsonify({"value": x})
   
if __name__ == '__main__':
     app.run()           