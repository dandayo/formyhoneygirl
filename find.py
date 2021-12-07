import urllib.request
import os
os.system('cls')

link = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date=2021-12-07"

open_link = urllib.request.urlopen(link)

data = open_link.read()

print(data)

metadata = {
    data
}

print(['url'])