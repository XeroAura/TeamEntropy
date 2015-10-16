#!/usr/bin/python

from bottle import route, run
import os
from time import strftime
import decipher

# Set time zone to Pittsburgh
os.environ['TZ'] = 'US/Eastern'
time.tzset()

@route('/q1')
def process():
	params = []
	message = decipher.decipher()
	time = strftime("%Y-%m-%d %H:%M:%S")
	page = "Team Entropy, 846185807052\n" + time + "\n" + message + "\n"
	return page

run(host='localhost', port=80)
