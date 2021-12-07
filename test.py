import urllib.request
import random
from datetime import date, timedelta
import os
import shutil
import requests
os.system('cls')


print(date.today() + timedelta(days=-1))
fist_date = date(1995, 6, 16)
last_date = (date.today())
print(last_date)

link = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=" + str(last_date)
print(link)

open_link = urllib.request.urlopen(link)

print("text:" + str(open_link.getcode()))

data = open_link.read()
print(data)
    
metadata = {
    open_link.read()
}

print(metadata["url"])