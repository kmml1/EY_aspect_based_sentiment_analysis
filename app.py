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
    randomTweets = dict()
    is_positive = False
    is_neutral = False
    is_negative = False
    for record in table:
        date = time.strptime(record[1], "%a %b %d %H:%M:%S %z %Y")
        str_date = str(date.tm_year) + " " + str(date.tm_mon) + " " + str(date.tm_mday)
        if str_date not in daily:
            daily[str_date] = {"positive": 0, "neutral": 0, "negative": 0}
        tmp = record[2]
        if tmp == 1:
            daily[str_date]["positive"] = daily[str_date]["positive"] + 1
            if not is_positive:
                randomTweets["positive"] = record[0]
                is_positive = True
        elif tmp == 0:
            daily[str_date]["neutral"] = daily[str_date]["neutral"] + 1
            if not is_neutral:
                randomTweets["neutral"] = record[0]
                is_neutral = True
        elif tmp == -1:
            daily[str_date]["negative"] = daily[str_date]["negative"] + 1
            if not is_negative:
                randomTweets["negative"] = record[0]
                is_negative = True

    if not is_positive:
        randomTweets["positive"] = " "
    if not is_neutral:
        randomTweets["neutral"] = " "
    if not is_negative:
        randomTweets["negative"] = " "

    dailyData = []
    sum_positive = 0
    sum_neutral = 0
    sum_negative = 0

    for day in daily:
        dailyData.append({"date": day, "positive": daily[day]["positive"], "neutral": daily[day]["neutral"],
                          "negative": daily[day]["negative"]})
        sum_positive = sum_positive + daily[day]["positive"]
        sum_negative = sum_negative + daily[day]["negative"]
        sum_neutral = sum_neutral + daily[day]["neutral"]

    out = dict()
    out["dailyData"] = dailyData
    out["positive"] = sum_positive
    out["neutral"] = sum_neutral
    out["negative"] = sum_negative
    out["randomTweets"] = randomTweets
    out["myDaily"] = daily

    return out


def fetch_data(tag):
    tmp_data = dict()
    if tag == "global":
        daily = dict()

        randomTweets = dict()
        randomTweets["positive"] = " "
        randomTweets["neutral"] = " "
        randomTweets["positive"] = " "
        is_positive = False
        is_neutral = False
        is_negative = False

        tmp_data["positive"] = 0
        tmp_data["neutral"] = 0
        tmp_data["negative"] = 0
        for hash_tag in hashtags:
            table = azureDBconnections.select(hash_tag)
            global_data = count_twitts(table)

            tmp_data["positive"] = tmp_data["positive"] + global_data["positive"]
            tmp_data["neutral"] = tmp_data["neutral"] + global_data["neutral"]
            tmp_data["negative"] = tmp_data["negative"] + global_data["negative"]

            for day in global_data["myDaily"]:
                if day not in daily:
                    daily[day] = {"positive": 0, "neutral": 0, "negative": 0}
                daily[day]["positive"] = daily[day]["positive"] + global_data["myDaily"][day]["positive"]
                daily[day]["neutral"] = daily[day]["neutral"] + global_data["myDaily"][day]["neutral"]
                daily[day]["negative"] = daily[day]["negative"] + global_data["myDaily"][day]["negative"]

            if not is_positive and len(global_data["randomTweets"]["positive"]) > 3:
                randomTweets["positive"] = global_data["randomTweets"]["positive"]
                is_positive = True
            if not is_neutral and len(global_data["randomTweets"]["neutral"]) > 3:
                randomTweets["neutral"] = global_data["randomTweets"]["neutral"]
                is_neutral = True
            if not is_negative and len(global_data["randomTweets"]["negative"]) > 3:
                randomTweets["negative"] = global_data["randomTweets"]["negative"]
                is_negative = True

        dailyData = []
        for day in daily:
            dailyData.append({"date": day, "positive": daily[day]["positive"], "neutral": daily[day]["neutral"],
                              "negative": daily[day]["negative"]})
        tmp_data["dailyData"] = dailyData
        tmp_data["randomTweets"] = randomTweets


    else:
        table = azureDBconnections.select(tag)
        tmp_data = count_twitts(table)

    tmp_data["hashtag"] = tag
    tmp_data["lastUpdate"] = str(datetime.today().year) + " " + str(datetime.today().month) + " " + str(
        datetime.today().day)
    return tmp_data.pop("myDaily")


@app.route('/')
def say_hello_world():
    return {"last_update_triggered": last_update, "planned_update": planned_update}


@app.route('/<hash_tag>')
def landing_page(hash_tag):
    if hash_tag == "global":
        return jsonify(fetch_data("global"))
    if hash_tag not in hashtags:
        return {"hash_tag": "invalid"}
    return jsonify(fetch_data(hash_tag))


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
            {"date": 20210126, "positive": 10, "neutral": 5, "negative": 7},
            {"date": 20210125, "positive": 15, "neutral": 5, "negative": 0},
            {"date": 20210124, "positive": 17, "neutral": 5, "negative": 1},
            {"date": 20210123, "positive": 12, "neutral": 5, "negative": 2},
            {"date": 20210122, "positive": 5, "neutral": 5, "negative": 4}
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
