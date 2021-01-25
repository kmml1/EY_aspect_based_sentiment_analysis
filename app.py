from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/hello')
def say_hello_world():
    return {'result': "W końcu kurwa"}