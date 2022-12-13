def main():

	f = open("input_day_12_p1", "r")

	grid = []

	x = 0
	y = 0
	cnt = 0
	for line in f:
		val = line.strip() # Removes white lj
		row = []
		for ch in list(line)[:-1]:
			if ch == '.':
				cnt += 1
			if ch == 'S':
				start = (x, y)
			elif ch == 'E':
				end = (x, y)
			row.append(ch)
			x += 1
		grid.append(row)
		y += 1

	f.close()

	# + 1 for E, + 2 because my mistake
	print(cnt + 1 + 2) 


if __name__ == "__main__":
	main()
