from flask import Flask
from flask_cors import CORS
from flask import jsonify

from datetime import datetime, timedelta
from threading import Timer

app = Flask(__name__)
CORS(app)

hashtags = ["kwarantanna", "vege", "IgaŚwiatek", "hot16challange", "fitness", "krolowezycia", "kryzys", "ikea", "łódź",
            "haloween", "kawa", "radom", "karmieniepiersia", "pomidorowa", "COVID19", "nvidia", "poniedziałek",
            "biedronka"]

json_out = {
    "hash_tag": "global",
    "date": 20210124,
    "positive": 0,
    "neutral": 0,
    "negative": 0,
}

last_update = datetime.today()


@app.route('/')
def say_hello_world():
    return {"last_update": last_update}


@app.route("/global")
def all_hashtags():
    json_out["hash_tag"] = "global"
    return jsonify(json_out)


@app.route('/<id>')
def landing_page(id):
    if id not in hashtags:
        return {"hash_tag": "invalid"}
    json_out["hash_tag"] = id
    return jsonify(json_out)


def db_trigger():
    x = datetime.today()
    global last_update
    last_update = datetime.today()
    y = x.replace(day=x.day, hour=0, minute=10, second=0, microsecond=0) + timedelta(minutes=1)
    delta_t = y - x
    secs = delta_t.total_seconds()
    t = Timer(secs, db_trigger)
    t.start()


db_trigger()
