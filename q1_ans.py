#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 19:30:34 2019

@author: aayushbhargava
"""

import requests
website='https://jsoneditoronline.herokuapp.com/v1/docs/774466adf5834d26bc7c839fe7b366ef'
i=requests.get(website)
k=i.json()
d=k['data']
o=d.split('start_time')
lis=[]
for x in o:
    try:
        j=x.split('"day_of_the_week": "')[1].split('",')[0]
    except:
        pass

print (list(set(lis)))