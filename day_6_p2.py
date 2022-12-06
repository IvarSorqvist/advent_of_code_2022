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
			substring = [] 
			for k in range(0, 14):
				substring.insert(0, line[i-k])
			substring.sort()
			for j in range(1,len(substring)):
				if substring[j] == substring[j-1]:
					unique = False
			if unique == True:
				print("Index: ", i+1)
				break


if __name__ == "__main__":
	main()
