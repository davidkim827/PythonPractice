#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

r = requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")

soup = BeautifulSoup(r.text, "html.parser")

with open('21-DecodeWebsiteText.txt', 'w') as openFile:
    for i in soup.find_all(class_="content-section"):
        for j in soup.find_all("p"):
            openFile.write(j.text)

openFile.close()