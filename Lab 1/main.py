#!/usr/bin/env python

import requests

print(requests.__version__)

r = requests.get("https://raw.githubusercontent.com/derrick-w/C404-Lab/master/Lab%201/main.py")

#print(r)

#print(dir(r))
print(r.text)
#print(r.status_code)

