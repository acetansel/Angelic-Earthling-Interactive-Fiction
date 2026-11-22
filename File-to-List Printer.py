def inputFile(error):
	while True:
		try:
			filename = open(input(), "r", encoding = "utf-8")
			return filename
		except FileNotFoundError:
			filename = open(input(error))
def filetoOneVarList(fileInQuestion):
	list = []
	for line in fileInQuestion:
		list.append(line.strip("\n"))
	return list
print(filetoOneVarList(inputFile("")))