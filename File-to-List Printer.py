def filetoOneVarList(fileInQuestion):
	list = []
	for line in fileInQuestion:
		list.append(line.strip("\n"))
	return list
file = filetoOneVarList(open("story.txt", "r", encoding = "utf-8"))
open("paragraphList.txt", "w", encoding = "utf-8").write(str(file))