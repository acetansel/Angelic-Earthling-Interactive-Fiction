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
def reversing(index, progressTo):
	sequence = []
	a = 0
	for i in range(1,progressTo):
		a += 2 ** i
		sequence.append(a)
	for n in range(sequence-1):
		if index > sequence[n] and not index > sequence[n+1]:
			coordLength = n + 1
	possibilities = []
	import random
	while True:
		guessCoordinate = ""
		for writing in range(coordLength):
			guessCoordinate += str(random.randint(0,1))
		if not guessCoordinate in possibilities:
			possibilities.append(guessCoordinate)
		if len(possibilities) == 2 ** coordLength:
			break		
	for possibility in possibilities:
		guess = determining(possibility)
		if guess == index:
			return possibility
	return None
def main():
	try:
		if input("Determining or Reversing? ").strip().lower()[0] == "d":
			print(determining(input()))
		else:
			print(reversing(input(), int(input())))
	except IndexError:
		print(reversing(input(), int(input())))
	except TypeError:
		print(reversing(input(), int(input())))
while True:
	main()