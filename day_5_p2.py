def main():
	print("Hello World")

	f = open("input_day_5", "r")

	file_input = [[],[],[],[],[],[],[],[],[]]
	instructions = []

	step = 1
	for line in f:
		if "FIRST" in line:
			step += 1
			continue
		if "SECOND" in line:
			step += 1
			continue

		if step == 1:
			value = line.strip()
			val = value.split(',')
			print(val)
			for i in range(0, len(val)):
				if ']' not in val[i]:
					continue
				file_input[i].append(val[i])
		elif step == 3:
			value = line.strip()
			instructions.append(value)

	f.close()


	print(file_input)
	print(instructions)

	for inst in instructions:
		inst_sp = inst.split(' ')
		move = inst_sp[1]
		fro  = inst_sp[3]
		to	 = inst_sp[5]

		print(move, fro, to)

		tmp_list = file_input[int(fro)-1][0:int(move)]
		file_input[int(fro)-1] = file_input[int(fro)-1][int(move):]
		old_file = file_input[int(to)-1]
#		file_input[int(to)-1].append(file_input[int(fro)-1].pop(0))
		file_input[int(to)-1] = tmp_list + file_input[int(to)-1]

		print(file_input)

	results = []

	for stack in file_input:
		print(stack[0])

if __name__ == "__main__":
	main()

