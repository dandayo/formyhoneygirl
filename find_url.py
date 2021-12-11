import json
import urllib.request
import random
from datetime import date, timedelta
import os
import shutil
import requests
os.system('cls')
os.system('cls')


last_date = (date.today())
yesterday = print(date.today() + timedelta(days=-1))
fist_date = date(1995, 6, 16)

link_today = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + \
    str(last_date)
link_yesterday = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + \
    str(yesterday)
link_random = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + str()

open_link = urllib.request.urlopen(link_today)

data = open_link.read()

data.decode('utf-8')
data = eval(data)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with open('data.json', 'r', encoding='utf-8') as s:
    image_url = json.load(s)
    print(image_url["url"])
