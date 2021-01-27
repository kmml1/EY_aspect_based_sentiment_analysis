#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.client, urllib.request, urllib.parse, urllib.error, base64
from twitter_program import credentials
import json


def sentiment(conn,text):
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
        #print(body)
        if (conn == None):
            conn = http.client.HTTPSConnection('northeurope.api.cognitive.microsoft.com')
        conn.request("POST", "/text/analytics/v2.1/sentiment?%s" % params, str(body).encode('utf-8'), headers)
        response = conn.getresponse()
        data = response.read()
        y = json.loads(data)
        

    except Exception as e:
        print("error cognitive services" + str(e.with_traceback) + str(e.__cause__))
    if 'documents' in y.keys():
        return y["documents"][0]["score"]
    print(y)
    return  0.5
def close(conn):
    conn.close()
def connect():
    conn = http.client.HTTPSConnection('northeurope.api.cognitive.microsoft.com')
    return conn
