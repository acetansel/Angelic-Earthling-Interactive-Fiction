import working
input("Return to start...")
print()
print("Welcome to the interactive fiction featuring a myriad web of what-ifs applied to Otitochukwu Eberendu's fantasy journal, Angelic Earthling.\nTo answer affirmatively to any question, type and submit any word that begins with Y and any word that begins with N to negatively answer. Now, we shall begin with a general synopsis:")
print()
input("Return to continue...")
print()
print("A story of all of humanity? No, this is a story of one blessed people graced with the spirit and power of a fallen angel and a two-blooded prince onto the land of Pacifia from since before the Great Flood. With it, their will to live drives to an unending end.")
print()
input("Return to continue...")
print()

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

