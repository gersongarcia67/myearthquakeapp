#!/usr/bin/python

import requests
import json

url='https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2014-01-01&endtime=2014-01-02'

response=requests.get(url)

if response.ok:

    jData=json.loads(response.content)

    for key in jData:
        print '==== START ===='
        print key+":"+str(jData[key])
        print '==== END ===='

else:

    response.raise_for_status()


