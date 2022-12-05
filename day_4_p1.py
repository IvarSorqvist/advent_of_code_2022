def main():
	print("Hello World")

	f = open("input", "r")

	file_input = []

	for line in f:
		file_t = []
		value = line.strip()
		pair = value.split(',')
		value_1 = pair[0].split('-')
		value_2 = pair[1].split('-')
		file_t.append(value_1)
		file_t.append(value_2)
		file_input.append(file_t)

	f.close()

	results = []

	sum = 0
	for i in file_input:
		if (int(i[0][0]) >= int(i[1][0]) and int(i[0][1]) <= int(i[1][1])) or \
		   (int(i[1][0]) >= int(i[0][0]) and int(i[1][1]) <= int(i[0][1])):
			sum += 1

	print(sum)

if __name__ == "__main__":
	main()

