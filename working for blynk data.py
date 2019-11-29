import json
import urllib.request
import requests
import threading
import time

def up():
    urlData = "https://api.thingspeak.com/channels/875168/feeds.json?api_key=4MX75FAP0HO8Z4WX&results=2"
    webURL = urllib.request.urlopen(urlData)
    data =json.loads( webURL.read().decode())
    x=data["feeds"][0]['field1']
    y=data["feeds"][0]['field2']
    URL = "http://blynk-cloud.com/0Mgw_IRUnX9HGiknP1smLiUWq86ygloG/update/v1?value="+str(x) 
    r = requests.get(url = URL) 
    print(y)
    print(x)

WAIT_TIME_SECONDS = 3

ticker = threading.Event()
#while not ticker.wait(WAIT_TIME_SECONDS):
up()
