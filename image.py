import shutil
import requests
import os
os.system('cls')



image_url = "https://apod.nasa.gov/apod/image/1709/astronomy101_hk_960.jpg"

filelName = image_url.split("/")[-1]+".jpg"

answer = requests.get(image_url, stream=True)

if answer.status_code == 200:
    answer.raw.decode_content = True

    with open(filelName, 'wb') as info:
        shutil.copyfileobj(answer.raw, info)

    print("Kuvanlataaminen onnistui", filelName)
else:
    print("Kuvaa ei voitu ladata.")