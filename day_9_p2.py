class Grid:

	def __init__(self):
		self.p_x = []
		self.p_y = []
		for i in range(10):
			self.p_x.append(0)
			self.p_y.append(0)
		self.T_pos = {"0,0" : 1}

	def check_close(self, p_x_1, p_y_1, p_x_2, p_y_2):
		""" return 2 for direct related,
				   1 for diagonal,
				   0 for not close """

		d_x = abs(p_x_1 - p_x_2)
		d_y = abs(p_y_1 - p_y_2)

		if d_x > 1 or d_y > 1:
			return -1
		elif d_x == 1 and d_y == 1:
			return 1
		elif d_x == 1 or d_y == 1:
			return 2
		else:
			return 0


	def mv_tail(self, i):

		alt_1_points = []

		for x in range(-1, 2):
			for y in range(-1, 2):
				if x == y == 0:
					continue
				points = self.check_close(self.p_x[i-1], self.p_y[i-1],
							     	      self.p_x[i]+x, self.p_y[i]+y)
				if points == 2:
					return x, y # Can only be one such place!
				elif points == 1:
					alt_1_points.append([x, y])

		if len(alt_1_points) != 1:
			print("alt_1_points need to be len 1")
			quit()

		return alt_1_points[0][0], alt_1_points[0][1]


	def mv(self, direction):
		if direction == 'R':
			self.p_x[0] += 1
		elif direction == 'U':
			self.p_y[0] += 1
		elif direction == 'L':
			self.p_x[0] -= 1
		elif direction == 'D':
			self.p_y[0] -= 1
		else:
			print("Wrong direction")
			quit()
		
		# The following part always tries to get as close as possible,
		# it can only move within its 8 pos parameter
		for i in range(1, len(self.p_x)):
			if (self.check_close(self.p_x[i-1], self.p_y[i-1],
								 self.p_x[i], self.p_y[i]) == -1):
				x, y = self.mv_tail(i)
				self.p_x[i] += x
				self.p_y[i] += y

		self.T_pos[f"{str(self.p_x[9])},{str(self.p_y[9])}"] = 1


	def print(self):
		print("x: ", self.p_x)
		print("y: ", self.p_y)
		for y in range(-20,20):
			line = ''
			for x in range(-20,20):
				ch = '.'
				for i in range(0, 10):
					if (x == self.p_x[i]) and (y == self.p_y[i]):
						ch = str(i)

				line += ch

			print(line)



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
		for i in range(int(inst[1])):
			# grid.print()
			grid.mv(inst[0])

	print("Tail pos length: ", len(grid.T_pos))


if __name__ == "__main__":
	main()
