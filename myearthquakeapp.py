#!/usr/bin/python

import requests
import json
from time import gmtime, strftime, localtime
from datetime import datetime



url='https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2018-06-05'

response=requests.get(url)

if response.ok:

    jData=json.loads(response.content)

    for feature in jData['features']:
        print '==== START ===='
        print feature['properties']['detail']
        print feature['properties']['place']
        print str(feature['properties']['mag'])
        print str(feature['geometry']['coordinates'])
        eqtime=feature['properties']['time']
        print str(eqtime)
        ms=eqtime/1000.0
        print str(datetime.utcfromtimestamp(ms))
        print '==== END ===='

else:

    response.raise_for_status()


