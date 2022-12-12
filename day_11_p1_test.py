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
		return old * 19

class Monkey1(Monkey):

	def new_calc(self, old):
		return old + 6

class Monkey2(Monkey):

	def new_calc(self, old):
		return old * old

class Monkey3(Monkey):

	def new_calc(self, old):
		return old + 3

class Monkey4(Monkey):

	def new_calc(self, old):
		return old * 19

def main():

	monkeys = []
	monkeys.append(Monkey0("monkey0",
						   [79, 98],
						   23))
	monkeys.append(Monkey1("monkey1",
						   [54, 65, 75, 74],
						   19))
	monkeys.append(Monkey2("monkey2",
						   [79, 60, 97],
						   13))
	monkeys.append(Monkey3("monkey3",
						   [74],
						   17))

	monkeys[0].monkey_true  = monkeys[2]
	monkeys[0].monkey_false = monkeys[3]
	monkeys[1].monkey_true  = monkeys[2]
	monkeys[1].monkey_false = monkeys[0]
	monkeys[2].monkey_true  = monkeys[1]
	monkeys[2].monkey_false = monkeys[3]
	monkeys[3].monkey_true  = monkeys[0]
	monkeys[3].monkey_false = monkeys[1]

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
