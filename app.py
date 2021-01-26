from flask import Flask
from flask_cors import CORS
from flask import jsonify

from datetime import datetime, timedelta
from threading import Timer

from twitter_program import azureDBconnections

last_update = None

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


def count_twitts(table):
    pass


def fetch_data(tag):
    tmp_data = []
    if tag == "global":
        for hash_tag in hashtags:
            table = azureDBconnections.select(tag)

    else:
        table = azureDBconnections.select(tag)
    return table


@app.route('/')
def say_hello_world():
    return {"last_update_triggered": last_update}


@app.route("/global")
def all_hashtags():
    #return jsonify(fetch_data("global")
    return "global"


@app.route('/<hash_tag>')
def landing_page(hash_tag):
    if hash_tag not in hashtags:
        return {"hash_tag": "invalid"}
    #return jsonify(fetch_data(hash_tag))
    return fetch_data(hash_tag)


def db_trigger():
    json_out["neutral"] = json_out["neutral"] + 1

    global last_update
    last_update = datetime.today()
    y = last_update.replace(day=last_update.day, hour=0, minute=10) + timedelta(days=1)
    delta_t = y - last_update
    secs = delta_t.total_seconds()
    t = Timer(secs, db_trigger)
    t.start()


db_trigger()
