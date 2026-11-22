def filetoOneVarList(fileInQuestion):
	list = []
	for line in fileInQuestion:
		list.append(line.strip("\n"))
	return list
print(filetoOneVarList(open("story.txt", "r", encoding = "utf-8")))