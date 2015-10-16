#!/usr/bin/python

import sys
import math

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
	size = math.sqrt(len(c))
	matrix = [[ c[j*size + i] for i in range(size)] for j in range(size)]
	i = ""
	for k in range(size):
		a = k
		b = 0
		while True:
			i.append(matrix[a][b])
			if a == 0:
				break
			else:
				a = a - 1
				b = b + 1

	# Shift message back Z characters
	message = ""
	for char in i:
		temp = ord(char)
		temp = temp + z
		message.append(chr(x if 97 <= x <= 122 else 96 + x % 122))

	print message

if __name__ == "__main__":
	decipher(sys.argv)
