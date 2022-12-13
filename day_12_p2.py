def main():

	f = open("input_day_12_2", "r")

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

	#min_steps
	#print(grid)
	#print(start, end)

	print(cnt)


if __name__ == "__main__":
	main()
