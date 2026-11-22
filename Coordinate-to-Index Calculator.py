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
	sequence = [0]
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
	while len(possibilities) < 2 ** coordLength:
		guessCoordinate = ""
		for i in range(coordLength):
			guessCoordinate += str(random.randint(0,1))
		if not guessCoordinate in possibilities:
			possibilities.append(guessCoordinate)
	for example in possibilities:
		guess = str(determining(example))
		if guess == index:
			return example
	return "Error 404"
def yes_no(question):
	answer = input(question)
	yes = True
	no = False
	if len(answer) == 0:
		return yes
	elif answer[0] == "Y":
		return yes
	elif answer[0] == "N":
		return no
	else:
		return no
def main():
	if yes_no("Determining? "):
		print(determining(input()))
	else:
		print(reversing(input()))
while True:
	main()