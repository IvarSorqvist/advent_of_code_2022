def main():
	print("Hello World")

	f = open("input", "r")

	file_input = []

	for line in f:
		value = line.strip()
		file_input.append(value)

	f.close()

	print("Len of array: ", len(file_input))

	# print(file_input)

	elf_max = 0
	current_elf = 0

	elfs = []

	for i in file_input:
		if i == '':
			elfs.append(current_elf)
			current_elf = 0
		else:
			current_elf += int(i)

	elfs.sort(reverse=True)
	print(elfs[0] + elfs[1] + elfs[2])
	print(elfs)
	print(elf_max)

if __name__ == "__main__":
	main()

