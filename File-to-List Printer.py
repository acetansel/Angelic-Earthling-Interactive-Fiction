def filetoOneVarList(fileInQuestion):
	list = []
	for line in fileInQuestion:
		list.append(line.strip("\n"))
	return list
open("paragraphs.txt", "w", encoding = "utf-8").write(str(filetoOneVarList(open("story.txt", "r", encoding = "utf-8"))))