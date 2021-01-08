# ETAssessment
copied from https://github.com/ianmcloughlin/random-app
Windows

FLASK
set FLASK_APP=windturbineprediction.py
python -m flask run

DOCKER
docker build . -t wind-image
docker run --name wind-container -d -p 5000:5000 wind-image