#!/usr/bin/env python
# File:        wikiDino.py
# Author:      Stephen
# Date:        11/1/2016
# Purpose:     Scrapes wikipedia for a list of dinosaurs and
#              converts to xml.
# Libraries:   BeautifulSoup4

# Library Imports
import urllib
import xml.etree.cElementTree as ET
import xml.dom.minidom
from bs4 import BeautifulSoup

# Sets wikipedia URL
url = 'https://en.wikipedia.org/wiki/List_of_dinosaur_genera'
print "Scrapping " + url

# Preps Beautiful Soup for scraping
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('a')

# Sets local variables
tot = 0
val = 0
count = 1
titles = []
excludes = ["bird", "reptile", "fish", "NoTitle", "Enlarge", 'Help:Category', 'Wikipedia:About']
dinoList = []

# Start scraping tags
for tag in tags:
    title = tag.get('title', 'NoTitle')
    titles.append(title)

# Refines scraped elements
for t in titles:
    # Checks for excluded items
    if t not in excludes:
        words = t.split()
        # Removes enteries longer than one word
        if len(words) == 1:
            dinoList.append(words)
            # Removes duplicates
            flat = [item for sublist in dinoList for item in sublist]
            flat = set(flat)
print "Scraped " + str(len(flat)) + " elements."

# XML output prep
root = ET.Element("dinosaurs")
child = ET.SubElement(root, "dinosaur")
name = ET.SubElement(child, "Name")
ID = ET.SubElement(child, "ID")

# Reads through list, converts to XML
print "Generating XML..."
for d in flat:
    count = count + 1
    did = str(count)
    child = ET.Element("dinosaur", ID=did)
    root.append(child)
    element = ET.SubElement(child, "Name").text= d

# Cleans up and writes XML file
xmlstr = xml.dom.minidom.parseString(ET.tostring(root)).toprettyxml()
with open("dinoXML.xml", "w") as f:
    f.write(xmlstr)
print "Done!"
