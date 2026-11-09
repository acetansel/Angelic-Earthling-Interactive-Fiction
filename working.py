def determining(key):
	if len(key) == 0:
		return 0
	level = 1
	minimum = 0
	for point in range (0,len(key)-1):
		minimum += 2 ** level
		level += 1
	shift = 0
	index = 0
	for value in key:
		if value == "0":
			shift += 2 ** (len(key) - 1 - index)
		index += 1
	shift += 1
	return minimum + shift

def lineuot():
	print("~" * 60)

def rightPrinting(block):
	scroll = block.split("*n*")
	for line in scroll:
		print(line)
		lineout()

def binaryQuestion(answer):
	while True:
		if answer[0] == "Y":
			return True
		elif answer[0] == "N":
			return False
		else:
			answer = input("Y/N?...").upper()
