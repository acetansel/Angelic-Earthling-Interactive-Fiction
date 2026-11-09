import working
input("Return to start...")
print("~" * 60)
print("Welcome to the interactive fiction with in an every-expanding tree of binary branches")
print("~" * 60)
print("To answer affirmatively to any question, type and submit any word that begins with Y and any word that begins with N to negatively answer.")
print("~" * 60)
input("Return to continue...")
print("~" * 60)

try:
	f = open("storyStrings.txt")
	draft = f.readlines()
	f.close()
	coordinates = ""

	while True:
		try:
			working.rightPrinting(draft[working.determining(coordinates)])
			answer = input().upper()
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

