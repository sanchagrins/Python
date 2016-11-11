#!/usr/bin/env python
# File:        linkGrabber.py
# Author:      Stephen
# Date:        11/11/2016
# Purpose:     Grabs all links from a given URL.
# Libraries:   BeautifulSoup4

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

tot = 0
val = 0
count = 0

for tag in tags:
    print tag.get('href', None)
