# first attempt at a python script ever

# write script to scrape REST service for state's data.
# grab the state number/district number (preferably state name as well), and coordinates.
# ogr2ogr the coordinate data, preferably with CLI tool called from script. //http://ogre.adc4gis.com/convert
# construct GEOJSON file from the results.
# ????
# profit
# file size considerations: may need to use topojson - https://github.com/topojson/topojson
# how did he do this? http://bl.ocks.org/mbostock/4060606
# https://d3js.org/us-10m.v1.json - here's what appears to be topojson used in the above. see if you can play around with it some.

import json
import requests


url = 'https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Legislative/MapServer/6/query?where=STATE%3D37&text=&objectIds=&time=&geometry=&geometryType=esriGeometryEnvelope&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=OBJECTID%2C+STATE%2C+NAME%2C+BASENAME&returnGeometry=true&returnTrueCurves=false&maxAllowableOffset=&geometryPrecision=&outSR=&returnIdsOnly=false&returnCountOnly=false&orderByFields=&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&resultOffset=&f=pjson'

#get JSON
response = requests.get(url)
data = response.json()

#need to force this for ogr2ogr to work.
data['spatialReference']['wkid'] = 3857


# create output JSON
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
