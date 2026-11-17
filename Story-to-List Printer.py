novel = open("story.txt", "r", encoding="utf-8-sig").readlines()
book = []
for line in novel:
	book.append(line.strip("\n"))
print(book)

