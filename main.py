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
	
def rightPrinting(block):
	scroll = block.split("*n*")
	for line in scroll:
		print(line)

def binaryQuestion(answer):
	while True:
		if answer[0] == "Y":
			return True
		elif answer[0] == "N":
			return False
		else:
			answer = input("Y/N?...").upper()

input("Return to start...")
print("Welcome to the interactive fiction featuring a myriad web of what-ifs applied to Otitochukwu Eberendu's fantasy journal, Angelic Earthling.\nTo answer affirmatively to any question, type and submit any word that begins with Y and any word that begins with N to negatively answer. Now, we shall begin with a general synopsis:")
input("Return to continue...")
print("A story of all of humanity? No, this is a story of one blessed people graced with the spirit and power of a fallen angel and a two-blooded prince onto the land of Pacifia from since before the Great Flood. With it, their will to live drives to an unending end.")
input("Return to continue...")

try:
	f = open("storyStrings.txt")
	draft = f.readlines()
	f.close()
	coordinates = ""

	while True:
		try:
			rightPrinting(draft[determining(coordinates)])
			answer = input().upper()
			answer += "answer"
			if binaryQuestion(answer):
				coordinates += "1"
			else:
				coordinates += "0"
		except IndexError:
			input("To be continued...Return to start over")
			coordinates = ""

except FileNotFoundError:
	print("Error retrieving story data...Make sure the storyStrings.txt file is present and retrievable.")
	input("Return to close...")

