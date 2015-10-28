#!/usr/bin/python

import sys
import os
import json
import calendar

# s3://cmucc-datasets/twitter/f15/

# Tweet id, sentiment score, censored tweet
# created_at, id_str, text, user["id_str"]
# Check for malformed

def main(argv):
	month = list(calendar.month_abbr)
	for line in sys.stdin:
		try:
			tweets = json.loads(line)
		except ValueError:
			print "Value Error"
			exit()

		try:
			time = tweets["created_at"]
			#          0   1  2     3        4    5
			# Convert Thu May 15 09:02:20 +0000 2014  TO  2014-05-31+01:29:04 
			contents = time.split(' ')
			monthnum = month.index(contents[1])
			time = contents[5] + "-" + str(monthnum).zfill(2) + "-" + contents[2] + "+" + contents[3]
			if(time < "2014-02-20+00:00:00")
				continue
			tweet_id = tweets["id_str"]
			user_id = tweets["user"]["id_str"]
			text = tweets["text"]
		except KeyError:
			print "Malformed tweet found."
			continue

		if time == "" or tweet_id == "" or user_id == "" or text == "":
			print ".",
			continue

		print "%s\t%s\t%s\t%s" % (user_id, tweet_id, time, json.dumps(text))


if __name__ == "__main__":
	main(sys.argv)
	