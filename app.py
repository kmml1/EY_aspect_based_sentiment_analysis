from flask import Flask
from flask_cors import CORS
from flask import jsonify
import time
import sys
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
            app.logger.info('starting connection')
            table = azureDBconnections.select(hash_tag)

            app.logger.info('connection end')
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
    app.logger.info('testing info log')
    print('Hello world!', file=sys.stderr)
    if hash_tag == "global":
        return jsonify(fetch_data("global"))
    if hash_tag not in hashtags:
        return {"hash_tag": "invalid"}
    return jsonify(fetch_data(hash_tag))


@app.route('/print')
def printMsg():
    app.logger.warning('testing warning log')
    app.logger.error('testing error log')
    app.logger.info('testing info log')
    return "Check your console"

@app.route('/test')
def testFront():
    return jsonify(
        hashtag="pomidorowa",
        positive=10000,
        neutral=5000, 
        negative=7000,
        lastUpdate=20210126,
        randomTweets={"positive": "Ale EZ", "neutral": "No prawie", "negative": "K@!@!"},
        dailyData=[
            {"date":20210126, "positive":10, "neutral":5, "negative":7},
            {"date":20210125, "positive":15, "neutral":5, "negative":0},
            {"date":20210124, "positive":17, "neutral":5, "negative":1},
            {"date":20210123, "positive":12, "neutral":5, "negative":2},
            {"date":20210122, "positive":5, "neutral":5, "negative":4}
        ]
    )

first_run = True


def db_trigger():
    time_now = datetime.today()
    global first_run
    if not first_run:
        global last_update
        last_update = datetime.today()
        # refresh db
        pass
    global planned_update
    planned_update = time_now.replace(day=time_now.day, hour=4, minute=30) + timedelta(days=1)
    delta_t = planned_update - time_now
    secs = delta_t.total_seconds()
    t = Timer(secs, db_trigger)
    t.start()
    first_run = False


db_trigger()
