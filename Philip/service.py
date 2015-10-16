#!/usr/bin/python

from bottle import route, run, request
import os
import time
from time import strftime
import decipher
import string

# Set time zone to Pittsburgh
os.environ['TZ'] = 'US/Eastern'
time.tzset()

@route('/q1')
def process():
	key = request.query.key
	cipher = request.query.message
	result = decipher.decipher(["decipher", key, cipher])
	time = strftime("%Y-%m-%d %H:%M:%S")
	page = "Team Entropy, 846185807052\n" + str(time) + "\n" + str(result) + "\n"
	return page

run(host='localhost', port=80)
# run(port=80) for real attempt
