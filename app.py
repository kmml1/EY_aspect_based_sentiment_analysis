from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
CORS(app)

hashtags = ["kwarantanna", "vege", "IgaŚwiatek", "hot16challange", "fitness", "krolowezycia", "kryzys", "ikea", "łódź",
            "haloween", "kawa", "radom", "karmieniepiersia", "pomidorowa", "COVID19", "nvidia", "poniedziałek",
            "biedronka"]

json_out = {
    "hash_tag": "global",
    "date": 20210124,
    "positive": 24800354,
    "neutral": 224398833,
    "negative": 224398833,
}


@app.route('/')
def say_hello_world():
    return jsonify(json_out)


@app.route("/global")
def hello():
    json_out["hash_tag"] = "global"
    return jsonify(json_out)


@app.route('/<id>')
def landing_page(id):
    if id not in hashtags:
        return {"hash_tag": "invalid"}
    json_out["hash_tag"] = id
    return jsonify(json_out)
