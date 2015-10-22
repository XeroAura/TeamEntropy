afinn = {}

# with open("afinn.txt") as f:
# 	for line in f:
# 		split = line.split()
# 		if len(split) == 2:
# 			afinn[split[0]] = split[1]

# 	print afinn

score = 0
cleared = re.sub('[^0-9a-zA-Z]+', ' ', text).lower()
for word in cleared.split(" "):
	if word in afinn:
		score = score + afinn[word]

print score
