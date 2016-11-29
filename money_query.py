# script to query followthemoney.org API.
# re = regexp

import sys
import re
import json
import requests
import pprint

pp = pprint.PrettyPrinter()


# H for house, S for senate
chamber = 'H'

# 2 letter state abbreviation
state = 'NC'

# independent expenditures vs. campaign contributions
spending_type = 'is'

# contributions
# url = 'http://api.followthemoney.org/?law-ot=' + chamber + '&law-s=' + state + '&gro=y,law-eid&APIKey=62cd51607343708af1510e08a94144ed&mode=json'

# independent expenditures
url = 'http://api.followthemoney.org/?dt=2&is-s=NC&is-r-ot=H&gro=is-t-tdis&APIKey=62cd51607343708af1510e08a94144ed&mode=json&so=is-t-tdis&sod=0'

# get JSON
response = requests.get(url)
data = response.json()


# function to sort the json.
def sort_by_int(json):
    try:
        # Also convert to int since update_time will be string.  When comparing
        # strings, "10" is smaller than "2".

        # some of the data will have "H" or "S" for house or senate.  this is already
        # defined, so let's remove it to make the data easier to work with.  basically
        # we use Regex to search for digit within the id, and force it to int.
        return int(re.search(r'\d+', json["Target_District"]["id"]).group())
    except (TypeError, KeyError, AttributeError):
        return 0

# sort data using sort function above
data = sorted(data["records"], key=sort_by_int, reverse=True)

# create output JSON (pretty printed)
with open('money.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
