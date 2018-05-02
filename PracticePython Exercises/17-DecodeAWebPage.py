#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

result = requests.get("https://www.nytimes.com")

c = result.content
soup = BeautifulSoup(c, "html.parser")

#h2 tag, 
d = soup.find_all("h2", {"class" : "story-heading"})
e = soup.find_all("h1", {"class" : "story-heading"})
count = 1

for i in d:
    title = i.text.strip()
    print("{}. {}".format(count, title))
    count += 1

for i in e:
    title = i.text.strip()
    print("{}. {}".format(count, title))
    count += 1
