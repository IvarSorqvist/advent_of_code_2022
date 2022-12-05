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
		#print(value_1, value_2)
		file_t.append(value_1)
		file_t.append(value_2)
		file_input.append(file_t)

	f.close()

	#print(file_input)

	results = []

	sum = 0
	for i in file_input:
		print(i)
		print(int(i[0][0]) in range(int(i[1][0]),int(i[1][1])+1))
		print(int(i[0][1]) in range(int(i[1][0]),int(i[1][1])+1))
		if int(i[0][0]) in range(int(i[1][0]),int(i[1][1])+1) or \
		   int(i[0][1]) in range(int(i[1][0]),int(i[1][1])+1) or \
		   int(i[1][0]) in range(int(i[0][0]),int(i[0][1])+1) or \
		   int(i[1][1]) in range(int(i[0][0]),int(i[0][1])+1):
			sum += 1
		print(sum)

	print(sum)
#
#	results_all = []  
#	for i in results:
#		results_all.append(points_dict[i])
#		sum += points_dict[i]
#
#	print(results_all)
#	print(sum)


if __name__ == "__main__":
	main()

