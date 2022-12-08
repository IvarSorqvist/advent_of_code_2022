def last_elem_hidden(ls):
	ls.reverse()
	len_visible = 0
	for i in range(1, len(ls)):
		len_visible += 1
		if ls[0] <= ls[i]:
			return len_visible

	return len_visible


def hidden_tree(matrix, x, y):
	tree_h = matrix[y][x]
	ls = []
	for i in range(0, x+1):
		ls.append(matrix[y][i])
	left = last_elem_hidden(ls)

	ls = []
	for i in range(0, y+1):
		ls.append(matrix[i][x])
	top = last_elem_hidden(ls)

	ls = []
	for i in range(len(matrix[y])-1, x-1, -1):
		ls.append(matrix[y][i])
	right = last_elem_hidden(ls)

	ls = []
	for i in range(len(matrix)-1, y-1, -1):
		ls.append(matrix[i][x])
	bottom = last_elem_hidden(ls)

	return left * top * right * bottom


def main():

	f = open("input_day_8", "r")

	file_input = []

	for line in f:
		val = line.strip() # Removes white spaces
		row = []
		for index in val:
			row.append(index)

		file_input.append(row)

	f.close()

	max_sc = 0
	for i in range(1, len(file_input)-1):
		for j in range(1, len(file_input[0])-1):
			hidden_trees = hidden_tree(file_input, j, i)
			if hidden_trees > max_sc:
				max_sc = hidden_trees
	
	print(max_sc)


if __name__ == "__main__":
	main()
