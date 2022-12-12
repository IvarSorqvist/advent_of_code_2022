class Monkey:

	def __init__(self, name, items, div):
		self.name = name
		self.items = items
		self.monkey_true = None
		self.mokey_false = None
		self.div = div
		self.inspections = 0

	def print(self):
		print(f"{self.name}: {self.items}")

	def print_inspections(self):
		print(f"{self.name}: {self.inspections}")

	def action(self):
		if len(self.items) == 0:
			return 0
		
		old = self.items.pop(0)
		print(f"Monkey inspects item with worry level {old}")
		new = self.new_calc(old)
		print(f"Worry level increases to {new}")
		new = new // 3
		print(f"Worry level is divided by 3 to {new}")
		if (new % self.div) == 0:
			print(f"Current worry level is divisible by {self.div}")
			print(f"Item with worry level {new} is thrown to {self.monkey_true.name}")
			self.monkey_true.items.append(new)
		else:
			self.monkey_false.items.append(new)
			print(f"Current worry level is not divisible by {self.div}")
			print(f"Item with worry level {new} is thrown to {self.monkey_false.name}")

		print("")

		self.inspections += 1

		return 1

class Monkey0(Monkey):

	def new_calc(self, old):
		return old * 11

class Monkey1(Monkey):

	def new_calc(self, old):
		return old + 4

class Monkey2(Monkey):

	def new_calc(self, old):
		return old * old

class Monkey3(Monkey):

	def new_calc(self, old):
		return old + 2

class Monkey4(Monkey):

	def new_calc(self, old):
		return old + 3

class Monkey5(Monkey):

	def new_calc(self, old):
		return old + 1

class Monkey6(Monkey):

	def new_calc(self, old):
		return old + 5

class Monkey7(Monkey):

	def new_calc(self, old):
		return old * 19

def main():

	monkeys = []
	monkeys.append(Monkey0("monkey0",
						   [63, 84, 80, 83, 84, 53, 88, 72],
						   13))
	monkeys.append(Monkey1("monkey1",
						   [67, 56, 92, 88, 84],
						   11))
	monkeys.append(Monkey2("monkey2",
						   [52],
						   2))
	monkeys.append(Monkey3("monkey3",
						   [59, 53, 60, 92, 69, 72],
						   5))
	monkeys.append(Monkey4("monkey4",
						   [61, 52, 55, 61],
						   7))
	monkeys.append(Monkey5("monkey5",
						   [79, 53],
						   3))
	monkeys.append(Monkey6("monkey6",
						   [59, 86, 67, 95, 92, 77, 91],
						   19))
	monkeys.append(Monkey7("monkey7",
						   [58, 83, 89],
						   17))

	monkeys[0].monkey_true  = monkeys[4]
	monkeys[0].monkey_false = monkeys[7]
	monkeys[1].monkey_true  = monkeys[5]
	monkeys[1].monkey_false = monkeys[3]
	monkeys[2].monkey_true  = monkeys[3]
	monkeys[2].monkey_false = monkeys[1]
	monkeys[3].monkey_true  = monkeys[5]
	monkeys[3].monkey_false = monkeys[6]
	monkeys[4].monkey_true  = monkeys[7]
	monkeys[4].monkey_false = monkeys[2]
	monkeys[5].monkey_true  = monkeys[0]
	monkeys[5].monkey_false = monkeys[6]
	monkeys[6].monkey_true  = monkeys[4]
	monkeys[6].monkey_false = monkeys[0]
	monkeys[7].monkey_true  = monkeys[2]
	monkeys[7].monkey_false = monkeys[1]

	for ro in range(20):
		for monkey in monkeys:
			print(monkey.name)
			while len(monkey.items) != 0:
				monkey.action()

		for monkey in monkeys:
			monkey.print()

	monkey_insp = []
	for monkey in monkeys:
		monkey.print_inspections()
		monkey_insp.append(monkey.inspections)

	monkey_insp.sort(reverse=True)
	print(monkey_insp)
	print(monkey_insp[0] * monkey_insp[1])




if __name__ == "__main__":
	main()
