#!/usr/bin/env python
# File:        linkGrabber.py
# Author:      Stephen
# Date:        11/11/2016
# Purpose:     Grabs all links from a given URL.
# Libraries:   BeautifulSoup4

import urllib
import xml.etree.cElementTree as ET
import xml.dom.minidom
from bs4 import BeautifulSoup

#url = raw_input('Enter URL: ')
url = 'https://en.wikipedia.org/wiki/List_of_dinosaur_genera'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')

tot = 0
val = 0
count = 1
titles = []
excludes = ["bird", "reptile", "fish", "NoTitle", "Enlarge", 'Help:Category', 'Wikipedia:About']
dinoList = []
for tag in tags:
    title = tag.get('title', 'NoTitle')
    #title.encode('ascii', 'ignore')
    titles.append(title)
for t in titles:
    if t not in excludes:
        #print t
        words = t.split()
        if len(words) == 1:
            dinoList.append(words)
            flat = [item for sublist in dinoList for item in sublist]
            flat = set(flat)
print flat

root = ET.Element("dinosaurs")
child = ET.SubElement(root, "dinosaur")
name = ET.SubElement(child, "Name")
ID = ET.SubElement(child, "ID")

for d in flat:
    count = count + 1
    did = str(count)
    child = ET.Element("dinosaur", ID=did)
    root.append(child)
    element = ET.SubElement(child, "Name").text= d
    #ET.SubElement(child, "ID").text = did
    #ET.SubElement(root, "NAME", ID=did).text = d
    #ET.SubElement(child, "NAME").text = d
    #ET.SubElement(name, "NAME").text = d
    #ET.SubElement(ID, "ID")

xmlstr = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
with open("NewXML.xml", "w") as f:
    f.write(xmlstr)

