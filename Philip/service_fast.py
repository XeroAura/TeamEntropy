#!/usr/bin/python

import gevent.monkey; gevent.monkey.patch_all()
import bottle
from bottle import route, run, request
import os
import time
from time import strftime
import string
import sys
import math


x = 8271997208960872478735181815578166723519929177896558845922250595511921395049126920528021164569045773
app = bottle.Bottle()

@app.route('/q1')
def process():
	xy = int(request.query.key)
	c = request.query.message
	z = 1 + (xy/x)%25

	# Convert Cipher to Intermediate text
	# i = intermediate message
	size = int(math.sqrt(len(c)))

	matrix = [[ c[j*size + i] for i in range(0, size)] for j in range(0, size)]
	i = ""
	# Top left half of matrix
	for k in range(0, size):
		a = k
		b = 0
		while True:
			i = i + matrix[b][a]
			if a == 0:
				break
			else:
				a = a - 1
				b = b + 1

	# Bottom right half of matrix
	for l in range(1, size):
		a = size-1
		b = l
		while True:
			i = i + matrix[b][a]
			if b == size-1:
				break
			else:
				a = a - 1
				b = b + 1


	# Shift message back Z characters
	shift = dict(zip(string.uppercase, string.uppercase[-z:] + string.uppercase[:-z]))
	result = ""
	for char in i:
		result = result + shift.get(char)

	time = strftime("%Y-%m-%d %H:%M:%S")
	page = "Team Entropy, 846185807052\n" + str(time) + "\n" + str(result) + "\n"
	return page


if __name__ == '__main__':
	# Set time zone to Pittsburgh
	os.environ['TZ'] = 'US/Eastern'
	time.tzset()
	print "Up and running"
	bottle.run(app=app, server='gevent', host='0.0.0.0', port=80, quiet=True)
