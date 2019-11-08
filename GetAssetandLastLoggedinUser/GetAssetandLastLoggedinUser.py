import requests
import json 
import os

# Import Enviroment variable
APITOKEN = os.environ.get('S1APITOKEN')
S1BASEURL = os.environ.get('S1BASETOKEN')
S1APIURL = os.environ.get('S1APIURL')

#Make API Call
url = S1APIURL+"agents?query=&limit=100"
querystring = {"apiToken":APITOKEN}
headers = {
    'Accept': "*/*",
    'Host': S1BASEURL,
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

# Response parsing
response = requests.request("GET", url, headers=headers, params=querystring)
responsejson = json.loads(response.text)
responsedata = (responsejson['data'])

# Open file for writing
openfile = open('S1Export.csv','w')

# Print Initial Entry and export to file
for assetid in responsedata:     
    addata = assetid['activeDirectory']
    compname = (assetid['computerName'])   
    lastuser = (assetid['lastLoggedInUserName'])
    sitename = (assetid['siteName'])
    s1data = (compname +","+ lastuser+","+sitename)
    openfile.write((s1data)+'\n'

# Print additional entries and paginate
cursor = (responsejson['pagination'])['nextCursor'] # pagination thing needed for S1 API. 
while cursor != None:
    cururl = url + "&cursor=" + cursor
    response = requests.request("GET", cururl, headers=headers, params=querystring)
    responsejson = json.loads(response.text)
    responsedata = (responsejson['data'])
    cursor = (responsejson['pagination'])['nextCursor']

    for assetid in responsedata:     
        addata = assetid['activeDirectory']
        compname = (assetid['computerName'])   
        lastuser = (assetid['lastLoggedInUserName'])
        sitename = (assetid['siteName'])
        s1data = (compname +","+ lastuser+","+sitename)
        openfile.write((s1data)+'\n')

# Close File
openfile.close()
