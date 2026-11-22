def determining(key):
	if len(key) == 0:
		return 0
	minimum = 0
	for point in range (1, len(key)):
		minimum += 2 ** point
	shift = 1
	for index in range(1,len(key)+1):
		if key[-index] == "1":
			shift += 2 ** (index - 1)
	return minimum + shift
def reversing(index):
	sequence = []
	a = 0
	for i in range(1,200):
		a += 2 ** i
		sequence.append(a)
	coordLength = 0
	for n in range(len(sequence) - 1) :
		if int(index) > sequence[n] and not int(index) > sequence[n+1]:
			coordLength = n + 1
	possibilities = []
	import random
	while len(possibilities) != 2 ** coordLength:
		guessCoordinate = ""
		for writing in range(coordLength):
			guessCoordinate += str(random.randint(0,2))
		if not guessCoordinate in possibilities:
			possibilities.append(guessCoordinate)	
	for possibility in possibilities:
		guess = determining(possibility)
		if guess == int(index):
			return possibility
	return "Couldn't retrieve the coordinate for",index,"the last guess being",guess
def main():
	if input("Determining or Reversing? ").strip().lower()[0] == "d":
		print(determining(input()))
	else:
		print(reversing(input()))
while True:
	main()