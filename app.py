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
    "positive": 0,
    "neutral": 0,
    "negative": 0,
}


@app.route('/')
def say_hello_world():
    return {"msg": "Hello Word"}


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


from datetime import datetime, timedelta
from threading import Timer


def db_trigger():
    json_out["positive"] = json_out["positive"] + 1
    x = datetime.today()
    #    #y = x.replace(day=x.day, hour=1, minute=0, second=0, microsecond=0) + timedelta(seconds=30)
    y = x + timedelta(seconds=30)
    delta_t = y - x
    secs = delta_t.total_seconds()
    t = Timer(secs, db_trigger)
    t.start()


db_trigger()
