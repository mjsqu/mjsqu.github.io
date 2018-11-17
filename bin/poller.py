#!/usr/bin/python
import requests
from datetime import datetime
import json,sys,os
from time import sleep

wgtn = [-41.300598, 174.780381]
dist = [100]

params = wgtn + dist

print(params)
url = "https://app.onzo.co.nz/nearby/%s/%s/%s"
url = url % tuple(params)

status = 0
while (status != 200):
  r = requests.get(url)
  status = r.status_code
  if status != 200:
     sleep(5)

datadir = os.path.dirname(sys.argv[0])
ofile = os.path.join(datadir,'..','data','onzo_%s.json' % datetime.now().strftime('%Y%m%d_%H%M%S'))

with open(ofile,'w') as f:
    f.write(r.content)
