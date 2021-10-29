from datetime import datetime
import requests
from time import sleep

while True:
#sleep(5)
    response = requests.get("https://github.com")
    if response.status_code != 200:
        print("github is down")
    else:
        print("github is ok")
print(datetime.now())
