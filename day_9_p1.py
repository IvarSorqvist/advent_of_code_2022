import json

class Grid:

	def __init__(self):
		self.pH_x = 0
		self.pH_y = 0
		self.pT_x = 0
		self.pT_y = 0
		self.T_pos = {"0,0" : 1}

	def mv_tail(self, direction):
		if direction == 'R':
			self.pT_x = self.pH_x - 1
			self.pT_y = self.pH_y
		elif direction == 'U':
			self.pT_x = self.pH_x
			self.pT_y = self.pH_y - 1
		elif direction == 'L':
			self.pT_x = self.pH_x + 1
			self.pT_y = self.pH_y
		elif direction == 'D':
			self.pT_x = self.pH_x
			self.pT_y = self.pH_y + 1

		self.T_pos[f"{str(self.pT_x)},{str(self.pT_y)}"] = 1

	def mv(self, direction):
		if direction == 'R':
			self.pH_x += 1
		elif direction == 'U':
			self.pH_y += 1
		elif direction == 'L':
			self.pH_x -= 1
		elif direction == 'D':
			self.pH_y -= 1
		else:
			print("Wrong direction")
			quit()

		if ((abs(self.pH_x - self.pT_x) > 1) or (abs(self.pH_y - self.pT_y) > 1)):
			self.mv_tail(direction)

		print(f"Dir: {direction}, H: ({self.pH_x}, {self.pH_y}), T: ({self.pT_x}, {self.pT_y})")
		print("len_dict: ", len(self.T_pos), str(self.pT_x) + str(self.pT_y))


def main():

	f = open("input_day_9", "r")

	file_input = []

	for line in f:
		val = line.strip() # Removes white spaces
		input = val.split()
		file_input.append(input)

	f.close()

	grid = Grid()

	for inst in file_input:
		print(inst)
		for i in range(int(inst[1])):
			grid.mv(inst[0])

	print("Tail pos length: ", len(grid.T_pos))

	print(json.dumps(grid.T_pos, indent=2))


if __name__ == "__main__":
	main()
