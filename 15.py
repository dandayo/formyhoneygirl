#from datetime import date, timedelta

#from random import randint

#import os

import urllib.request
import random
from datetime import date, timedelta
import os
import shutil
import requests
os.system('cls')

def paaohjelma():
    last_date = (date.today())
    yesterday = print(date.today() + timedelta(days=-1))
    fist_date = date(1995, 6, 16)
  
    

    link_today = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + str(last_date)
    link_yesterday = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + str(yesterday)
    link_random = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + str()

    open_link = urllib.request.urlopen(link_today)

    metadata = {
        open_link
    }

    
    image_url = metadata["url"]

    filelName = image_url.split("/")[-1]+".jpg"

    answer = requests.get(image_url, stream=True)

    if answer.status_code == 200:
        answer.raw.decode_content = True

        with open(filelName, 'wb') as info:
            shutil.copyfileobj(answer.raw, info)

        print("Kuvanlataaminen onnistui", filelName)
    else:
        print("Kuvaa ei voitu ladata.")

