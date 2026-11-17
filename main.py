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
		if value == "1":
			shift += 2 ** (len(key) - 1 - index)
		index += 1
	shift += 1
	return minimum + shift

def lineout():
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
input("Return to start...")
lineout()
print("Welcome to the interactive fiction with in an every-expanding tree of binary branches")
lineout()
print("To answer affirmatively to any question, type and submit any word that begins with Y and any word that begins with N to negatively answer.")
lineout()
input("Return to continue...")
lineout()

try:
	novel = open("story.txt", "r")
	coordinates = ""

	while True:
		try:
			rightPrinting(novel[determining(coordinates)])
			answer = input().upper()
			lineout()
			answer += "buffer"
			if binaryQuestion(answer):
				coordinates += "1"
			else:
				coordinates += "0"
		except IndexError:
			input("To be continued...Return to start over")
			coordinates = ""

except FileNotFoundError:
	print("Error retrieving story data...Make sure the story.txt file is present and retrievable.")
	input("Return to close...")

