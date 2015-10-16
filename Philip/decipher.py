#!/usr/bin/python

import sys
import math
import string

def decipher(argv):
	if len(argv) != 3:
		print "Usage: ./decipher.py [XY] [C]"
		sys.exit(1)

	# X - Secret Key
	# Y - Message key
	# C - Ciphertext
	# Z - Intermediate key = 1 + Y % 25
	# URL contains X*Y and C

	x = 8271997208960872478735181815578166723519929177896558845922250595511921395049126920528021164569045773
	xy = int(argv[1])
	c =  argv[2]

	y = xy/x
	z = 1 + y%25

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
	shift = dict(zip(string.lowercase, string.lowercase[z:] + string.lowercase[:z]))
	shift.update(zip(string.uppercase, string.uppercase[z:] + string.uppercase[:z]))
	message = ""
	for char in i:
		message = message + shift.get(char)
	return message

if __name__ == "__main__":
	decipher(sys.argv)
