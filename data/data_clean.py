# script to clean data
# re = regexp
import sys
import re
import csv
import operator


# function to clean the data using regexp
def re_int(string):
    try:
        # some of the data will have "H" or "S" for house or senate, or "DISTRICT", etc.  this is already
        # defined, so let's remove it to make the data easier to work with.  basically
        # we use Regex to search for digit within the id, and force it to int.
        return int(re.search('\d+', string).group())
    except (TypeError, KeyError, AttributeError):
        return 0


# create output TSV sorted and cleaned
readfile = csv.reader(open('ncga-independent.tsv'),delimiter='\t')


# writefile = csv.reader(open('new.tsv'),delimiter='\t')
with open('new.tsv', 'w', newline='') as myTSV:
    writefile = csv.writer(myTSV,delimiter='\t')
    for row in readfile:
        try:
            parsed_district = re_int(row[2])
            if(parsed_district != 0):
                writefile.writerow([parsed_district, row[5]])
        except (IndexError):
            pass
