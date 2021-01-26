#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.client, urllib.request, urllib.parse, urllib.error, base64
import credentials
import json


def sentiment(text):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': credentials.key,
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'showStats': '{boolean}'
    })

    try:
        body = {
            "documents": [
                {
                    "language": "pl",
                    "id": "1",
                    "text": text
                }
            ]
        }
        # print(body)
        conn = http.client.HTTPSConnection('northeurope.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.1/sentiment?%s" % params, str(body).encode('utf-8'), headers)
        response = conn.getresponse()
        data = response.read()
        y = json.loads(data)
        conn.close()

    except Exception as e:
        print("error cognitive services" + e.with_traceback + e.__cause__)
    if 'documents' in y.keys():
        return y["documents"][0]["score"]
    return 0.5


def test():
    s = "Nie lubię polaków."
    print(s + "  " + str(sentiment(s)))

    s = "Lubię polaków."
    print(s + "  " + str(sentiment(s)))

    s = "Jebać polaków."
    print(s + "  " + str(sentiment(s)))

    s = "Kocham polaków."
    print(s + "  " + str(sentiment(s)))

    s = "Nienawidzę polaków."
    print(s + "  " + str(sentiment(s)))

    s = "Polacy sie nie myją i smierdzą."
    print(s + "  " + str(sentiment(s)))

    s = "Polacy to złodzieje."
    print(s + "  " + str(sentiment(s)))

    """
    #############################ANG
    s = "I don't like polish people." 
    print(s + "  " + str(sentiment(s)))
    s = "I do like polish people."
    print(s + "  " + str(sentiment(s)))
    s = "Fuck polish people."
    print(s + "  " + str(sentiment(s)))
    s = "I love polish people."
    print(s + "  " + str(sentiment(s)))
    s = "I hate polish people."
    print(s + "  " + str(sentiment(s)))
    s = "Polish people smell bad"
    print(s + "  " + str(sentiment(s)))
    s = "Polish people are thieves"
    print(s + "  " + str(sentiment(s)))
    """
