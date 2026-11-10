import working
input("Return to start...")
working.lineout()
print("Welcome to the interactive fiction with in an every-expanding tree of binary branches")
working.lineout()
print("To answer affirmatively to any question, type and submit any word that begins with Y and any word that begins with N to negatively answer.")
working.lineout()
input("Return to continue...")
working.lineout()

try:
	f = open("storyStrings.txt")
	draft = f.readlines()
	f.close()
	coordinates = ""

	while True:
		try:
			working.rightPrinting(draft[working.determining(coordinates)])
			answer = input().upper()
			working.lineout()
			answer += "answer"
			if working.binaryQuestion(answer):
				coordinates += "1"
			else:
				coordinates += "0"
		except IndexError:
			input("To be continued...Return to start over")
			coordinates = ""

except FileNotFoundError:
	print("Error retrieving story data...Make sure the storyStrings.txt file is present and retrievable.")
	input("Return to close...")

