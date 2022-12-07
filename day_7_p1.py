total_size = 0

class File:
	def __init__(self, name, size):
		self.size = int(size)
		self.name = name

	def print(self, white_space):
		print("{} - {} {} (file)".format(white_space, self.name, self.size))


class Directory:

	def __init__(self, name, parent):
		self.name = name
		self.parent = parent
		self.dir_childs = {} 
		self.files = []
	
	def print(self, white_space):
		print("{} - {} (dir)".format(white_space, self.name))
		for key in self.dir_childs:
			self.dir_childs[key].print(white_space + " ")
		for fi in self.files:
			fi.print(white_space + " ")

	def cur_child(self, child):
		if child not in self.dir_childs:
			return None
		else:
			return self.dir_childs[child]

	def add_dir_child(self, child_name):
		print(self.dir_childs)
		self.dir_childs.update({child_name: Directory(child_name, self)})

	def get_size(self):
		global total_size
		size_files = 0
		for fi in self.files:
			size_files += fi.size

		size_dir = 0
		for key in self.dir_childs:
			size_dir += self.dir_childs[key].get_size()
		
		tot_size = size_files + size_dir
		if tot_size <= 100000:
			total_size += tot_size
		return tot_size


def main():

	f = open("input_day_7", "r")

	file_input = {}
	cur_path = []

	cur_dir = Directory('/', None)

	first = True
	for line in f:
		if first:
			first = False
			continue
			
		value = line.strip() # Removes white spaces
		val = value.split()
		if val[0] == '$':
			if val[1] == 'cd':
				if val[2] == '..':
					cur_dir = cur_dir.parent
				else:
					cur_dir = cur_dir.cur_child(val[2])
		elif val[0] == 'dir':
			cur_dir.add_dir_child(val[1])
		else:
			new_file = File(val[1], val[0])
			cur_dir.files.append(new_file)

	f.close()

	while cur_dir.name != '/':
		cur_dir = cur_dir.parent

	cur_dir.print("")
	total_s = cur_dir.get_size()
	print(total_size)


if __name__ == "__main__":
	main()
