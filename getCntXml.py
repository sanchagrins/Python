#!/usr/bin/env python
# File:    getCntXml.py
# Author:  sancahgrins
# Date:    11/17/2016
# Purpose: Sums the <count> field from a xml file
#          URL: http://python-data.dr-chuck.net/comments_320789.xml

import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter URL: ')
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved', len(data), 'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')
lst = tree.findall('comments/comment')
print 'Count: ', len(counts)

cnt = 0
for item in lst:
    cnt = cnt + int(item.find('count').text)
print 'Sum: ', cnt    
