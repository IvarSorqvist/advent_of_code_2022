def last_elem_hidden(ls):
	for i in range(0, len(ls)-1):
		if ls[i] >= ls[len(ls)-1]:
			return True # Hidden

	return False # Visible


def hidden_tree(matrix, x, y):
	tree_h = matrix[y][x]
	ls = []
	for i in range(0, x+1):
		ls.append(matrix[y][i])
	if not last_elem_hidden(ls):
		return 0

	ls = []
	for i in range(0, y+1):
		ls.append(matrix[i][x])
	if not last_elem_hidden(ls):
		return 0

	ls = []
	for i in range(len(matrix[y])-1, x-1, -1):
		ls.append(matrix[y][i])
	if not last_elem_hidden(ls):
		return 0

	ls = []
	for i in range(len(matrix)-1, y-1, -1):
		ls.append(matrix[i][x])
	if not last_elem_hidden(ls):
		return 0

	return 1


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

	hidden_trees = 0
	for i in range(1, len(file_input)-1):
		for j in range(1, len(file_input[0])-1):
			hidden_trees += hidden_tree(file_input, j, i)
	
	print("Hidden trees: ", hidden_trees)
	print("Visible trees: ", len(file_input)*len(file_input[0]) - hidden_trees)


if __name__ == "__main__":
	main()
