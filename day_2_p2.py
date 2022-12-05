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

	results = []

	# X Lose
	# Y Draw
	# Z Win

	for i in file_input:
		split = i.split()
		if split[1] == 'X': # Lose
			if split[0] == 'A':
				win_p = 0
				choice_p = 3
			elif split[0] == 'B':
				win_p = 0
				choice_p = 1
			elif split [0] == 'C':
				win_p = 0
				choice_p = 2

		elif split[1] == 'Y': # Draw
			if split[0] == 'A':
				win_p = 3
				choice_p = 1
			elif split[0] == 'B':
				win_p = 3
				choice_p = 2
			elif split [0] == 'C':
				win_p = 3
				choice_p = 3
		elif split[1] == 'Z': # Win
			if split[0] == 'A':
				win_p = 6
	  			choice_p = 2
			elif split[0] == 'B':
				win_p = 6
				choice_p = 3
			elif split [0] == 'C':
				win_p = 6
				choice_p = 1
		print(choice_p, win_p)

		results.append(choice_p + win_p)

	print(sum(results))


if __name__ == "__main__":
	main()

