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
def main():			
	input("Return to start...")
	lineout()
	print("To answer affirmatively to any question, return any word that begins with Y.")
	print("To answer negatively to any question, return any word that begins with N.")
	lineout()
	input("Return to continue...")
	lineout()
	
	try:
		f = open("story.txt")
		movel = f.readlines()
		f.close()
		coordinates = ""
	
		while True:
			try:
				rightPrinting(novel[determining(coordinates)])
				answer = input().upper() + "X"
				lineout()
				if binaryQuestion(answer):
					coordinates += "1"
				else:
					coordinates += "0"
			except IndexError:
				if len(input("You have reached the end of this branch...The story shall be continued.\nReturn something to start over and return nothing to close.")) == 0:
					break
				coordinates = ""
	
	except FileNotFoundError:
		input("Error retrieving story data...Make sure the story.txt file is present and retrievable.\nReturn to close...")

main()
		
	
