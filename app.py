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


@app.route("/global")
def hello():
    return "global hello"


h1 = "/kwarantanna"


@app.route(h1)
def hello():
    return "Hello, World!", h1


h2 = "/vege"


@app.route(h2)
def hello():
    return "Hello, World!", h2


h3 = "/IgaŚwiatek"


@app.route(h3)
def hello():
    return "Hello, World!", h3


h4 = "hot16challange"


@app.route(h3)
def hello():
    return "Hello, World!", h4


h5 = "fitness"


@app.route(h3)
def hello():
    return "Hello, World!", h5


h6 = "krolowezycia"


@app.route(h3)
def hello():
    return "Hello, World!", h6


h7 = "kryzys"


@app.route(h3)
def hello():
    return "Hello, World!", h7


h8 = "ikea"


@app.route(h3)
def hello():
    return "Hello, World!", h8


h9 = "łódź"


@app.route(h3)
def hello():
    return "Hello, World!", h9


h10 = "haloween"


@app.route(h3)
def hello():
    return "Hello, World!", h10


h11 = "kawa"


@app.route(h3)
def hello():
    return "Hello, World!", h11


h12 = "radom"


@app.route(h3)
def hello():
    return "Hello, World!", h12


h13 = "karmieniepiersia"


@app.route(h3)
def hello():
    return "Hello, World!", h13


h14 = "pomidorowa"


@app.route(h3)
def hello():
    return "Hello, World!", h14


h15 = "COVID19"


@app.route(h3)
def hello():
    return "Hello, World!", h15


h16 = "nvidia"


@app.route(h3)
def hello():
    return "Hello, World!", h16


h17 = "poniedziałek"


@app.route(h3)
def hello():
    return "Hello, World!", h17


h18 = "biedronka"


@app.route(h3)
def hello():
    return "Hello, World!", h18

# {
#   "date": 20210124,
#   "positive": 24800354,
#   "neutral": 224398833,
#   "negative": 224398833,
# },
