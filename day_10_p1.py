class CPU():

	def __init__(self, inst):
		self.inst = inst
		self.V = 1
		self.clk = 0
		self.sign_strength = []
		self.tot_sign_strength = 0
		self.current_inst = None
		self.addx_first_cycle = False

	def check_sign_strength(self):
		if (self.clk == 20) or (((self.clk - 20) % 40) == 0):
			self.sign_strength.append(self.V * self.clk)

	def clk_tick(self):
		self.clk += 1 # New cycle
		self.check_sign_strength()
		if (len(self.inst) == 0) and not self.addx_first_cycle:
			return True

		if self.addx_first_cycle:
			self.addx_first_cycle = False
			self.V += int(self.current_inst[1])
		else:
			self.current_inst = self.inst.pop(0)
			if self.current_inst[0] == 'noop':
				return False
	
			if self.current_inst[0] == 'addx':
				self.addx_first_cycle = True


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

	print("Done ", sum(cpu.sign_strength))

if __name__ == "__main__":
	main()
