def main():
	print("Hello World")

	f = open("input", "r")

	file_input = []

	for line in f:
		value = line.strip() # Removes white spaces
		file_input.append(value)

	f.close()

	unique = True
	for line in file_input:
		for i in range(13, len(line)):
			unique = True
			substring = line[i-3] + line[i-2] + line[i-1] + line[i]
			lst = list(substring)
			lst.sort()
			for j in range(1,len(lst)):
				if lst[j] == lst[j-1]:
					unique = False
			if unique == True:
				print("Index: ", i+1)
				break


if __name__ == "__main__":
	main()
