def main():
	print("Hello World")

	f = open("input", "r")

	file_input = []

	for line in f:
		value = line.strip()
		file_input.append(value)

	f.close()

	print("Len of array: ", len(file_input))

	print(file_input)

	elf_max = 0
	current_elf = 0

	for i in file_input:
		if i == '':
			print("New elf")
			if current_elf > elf_max:
				print("New max ", current_elf, " Old max ", elf_max)
				elf_max = current_elf	
			current_elf = 0
		else:
			# print(i)
			current_elf += int(i)

	print(elf_max)

#	count = 0
#	for i in range(1, len(file_input)):
#		print(i, file_input[i])
#		if file_input[i] >= file_input[i-1]:
#			count += 1
#
#	print("COUNT: ", count)

if __name__ == "__main__":
	main()

