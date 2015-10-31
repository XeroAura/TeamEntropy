#!/usr/bin/python

import sys
import os
import csv
import json

# Check for repeats by storing tweet id while processing tweets from each user id
# Process afinn 
# Process censoring

def main(argv):
	writer = csv.writer(sys.stdout, lineterminator='\n')

	for row in sys.stdin: # Gives the row as a list
		line = row.split('\t', 1)
		try:
			dat = json.loads(line[1])
		except ValueError:
			# print "Value Error"
			continue
			
		# Write out the format desired (csv)
		writer.writerow(dat)

if __name__ == "__main__":
	main(sys.argv)
