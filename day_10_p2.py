class CPU():

	def __init__(self, inst):
		self.inst = inst
		self.V = 1
		self.clk = 0
		self.current_inst = None
		self.addx_first_cycle = False
		self.CRT = [[], [], [], [], [], []]

	def add_draw(self):
		row = (self.clk - 1) // 40
		column = (self.clk - 1) % 40

		if (self.V - column >= -1) and (self.V - column <= 1):
			self.CRT[row].append('#')
		else:
			self.CRT[row].append(' ')


	def clk_tick(self):
		self.clk += 1 # New cycle
		if (len(self.inst) == 0) and not self.addx_first_cycle:
			return True

		if self.addx_first_cycle:
			self.addx_first_cycle = False
			self.add_draw()
			self.V += int(self.current_inst[1])
		else:
			self.current_inst = self.inst.pop(0)
			self.add_draw()
			if self.current_inst[0] == 'noop':
				return False
			if self.current_inst[0] == 'addx':
				self.addx_first_cycle = True

	def print(self):
		for r in self.CRT:
			row = ''
			for c in r:
				row += c
			print(row)


def main():

	f = open("input_day_10", "r")

	file_input = []

	for line in f:
		val = line.strip() # Removes white spaces
		input = val.split()
		file_input.append(input)

	f.close()

	cpu = CPU(file_input)

	while (True):
		if cpu.clk_tick():
			break

	cpu.print()

if __name__ == "__main__":
	main()
