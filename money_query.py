import json
import requests

url = 'http://api.followthemoney.org/?law-ot=H&law-s=NC&gro=y,law-eid&APIKey=62cd51607343708af1510e08a94144ed&mode=json'

# get JSON
response = requests.get(url)
data = response.json()

# create output JSON
with open('money.json', 'w') as outfile:
    json.dump(data, outfile)
