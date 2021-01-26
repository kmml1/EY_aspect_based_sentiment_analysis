from flask import Flask
from flask_cors import CORS
from flask import jsonify
import time

from datetime import datetime, timedelta
from threading import Timer

from twitter_program import azureDBconnections

last_update = None
planned_update = None

app = Flask(__name__)
CORS(app)

hashtags = ["kwarantanna", "vege", "IgaŚwiatek", "hot16challange", "fitness", "krolowezycia", "kryzys", "ikea", "łódź",
            "haloween", "kawa", "radom", "karmieniepiersia", "pomidorowa", "COVID19", "nvidia", "poniedziałek",
            "biedronka"]


def count_twitts(table):
    daily = dict()
    for record in table:
        date = time.strptime(record[1], "%a %b %d %H:%M:%S %z %Y")
        str_date = str(date.tm_year) + ", " + str(date.tm_mon) + ", " + str(date.tm_mday)
        if str_date not in daily:
            daily[str_date] = {"positive": 0, "neutral": 0, "negative": 0, }
        tmp = record[2]
        if tmp == 1:
            daily[str_date]["positive"] = daily[str_date]["positive"] + 1
        elif tmp == 0:
            daily[str_date]["neutral"] = daily[str_date]["neutral"] + 1
        elif tmp == -1:
            daily[str_date]["negative"] = daily[str_date]["negative"] + 1
    return daily


def fetch_data(tag):
    tmp_data = []
    if tag == "global":
        for hash_tag in hashtags:
            table = azureDBconnections.select(hash_tag)
            counted = count_twitts(table)
            tmp_data.append({"hash_tag": hash_tag, "data": counted})
    else:
        table = azureDBconnections.select(tag)
        counted = count_twitts(table)
        tmp_data.append({"hash_tag": tag, "data": counted})
    return tmp_data


@app.route('/')
def say_hello_world():
    return {"last_update_triggered": last_update, "planned_update": planned_update}


@app.route('/<hash_tag>')
def landing_page(hash_tag):
    if hash_tag == "global":
        if hash_tag not in hashtags:
            return {"hash_tag": "invalid"}
    return jsonify(fetch_data(hash_tag))


first_run = True


def db_trigger():
    time_now = datetime.today()
    global first_run
    if not first_run:
        global last_update
        last_update = time_now
        # refresh db
        pass
    global planned_update
    planned_update = last_update.replace(day=last_update.day, hour=4, minute=30) + timedelta(days=1)
    delta_t = planned_update - time_now
    secs = delta_t.total_seconds()
    t = Timer(secs, db_trigger)
    t.start()
    first_run = False


db_trigger()
