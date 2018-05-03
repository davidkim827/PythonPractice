#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.youtube.com")

soup = BeautifulSoup(result.text, "html.parser")

d = soup.find_all(class_="style-scope ytd-grid-video-renderer")
count = 1

for i in d:
    for j in soup.find_all("a"): 
        print("{}. {}".format(count, j.text))
    count += 1
