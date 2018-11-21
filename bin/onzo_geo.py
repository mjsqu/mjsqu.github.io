#!/usr/bin/python
import matplotlib.path as mpp
import numpy as np
import json

with open('../data/ref/Wellington_AU_Shapes.json','r') as f:
  wgtn_au = json.load(f)

print(wgtn_au[0])

geo = '\ufeffWKT'
name = 'AU_
