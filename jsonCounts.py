import urllib
import json

url = raw_input("Enter JSON URL: " )
#url = 'http://python-data.dr-chuck.net/comments_42.json'
#url = 'http://python-data.dr-chuck.net/comments_320793.json'

print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'
#print data

jdata = json.loads(str(data))
print 'Count:',len(jdata)

js = jdata["comments"]

sumCnt = 0
for item in js:
    sumCnt = sumCnt + item["count"]
print 'Sum',sumCnt
