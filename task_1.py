"""Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc.

"""

# Solution:

import requests

url = 'https://en.wikipedia.org/robots.txt'

# requests.get(url)

resp = requests.get(url)

# help(resp)

# print(resp.status_code)

# print(resp.ok)

# print(resp.text)

# print(resp.content)

with open('robots.txt', 'w', encoding='utf-8') as g:
    g.write(resp.text)
