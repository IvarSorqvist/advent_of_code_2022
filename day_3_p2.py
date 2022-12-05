def main():
	print("Hello World")

	f = open("input", "r")

	file_input = []

	count = 0
	group = []
	for line in f:
		count += 1
		value = line.strip()
		group.append(value)
		if count == 3:
			count = 0
			file_input.append(group)
			group = []

	f.close()

	print ( file_input) 

	points_dict ={
		"a" : 1,
		"b" : 2,
		"c" : 3,
		"d" : 4,
		"e" : 5,
		"f" : 6,
		"g" : 7,
		"h" : 8,
		"i" : 9,
		"j" : 10,
		"k" : 11,
		"l" : 12,
		"m" : 13,
		"n" : 14,
		"o" : 15,
		"p" : 16,
		"q" : 17,
		"r" : 18,
		"s" : 19,
		"t" : 20,
		"u" : 21,
		"v" : 22,
		"w" : 23,
		"x" : 24,
		"y" : 25,
		"z" : 26,
		"A" : 27,
		"B" : 28,
		"C" : 29,
		"D" : 30,
		"E" : 31,
		"F" : 32,
		"G" : 33,
		"H" : 34,
		"I" : 35,
		"J" : 36,
		"K" : 37,
		"L" : 38,
		"M" : 39,
		"N" : 40,
		"O" : 41,
		"P" : 42,
		"Q" : 43,
		"R" : 44,
		"S" : 45,
		"T" : 46,
		"U" : 47,
		"V" : 48,
		"W" : 49,
		"X" : 50,
		"Y" : 51,
		"Z" : 52
	}

	print("Len of array: ", len(file_input))

	print(file_input)

	results = []

	for group in file_input:
		lm1 = []
		lm2 = []
		for letter_0 in group[0]:
			if letter_0 in group[1]:
				if letter_0 in group[2]:
					results.append(letter_0)
					break

	print(results)

	print(len(file_input), len(results))


	results_all = []  
	sum = 0
	for i in results:
		results_all.append(points_dict[i])
		sum += points_dict[i]


#jk		print(double, double_plus)



#		print(split1, split2)
	print(results_all)
	print(sum)

#	print(sum(results_all))


if __name__ == "__main__":
	main()

