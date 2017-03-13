import random

class physical_mem:
	def __init__(self, size):
		self.s = size
		self.mem = {}

	def clock():
		for x in self.mem:
			self.mem[1] = 0

	def contains(frame_id):
		return frame_id in self.mem

	def put(frame_id): # data, referenced, modified
		self.mem[frame_id] = ("data", 1, 1)

	def access(frame_id, mode): # mode true if write, false if read
		if contains(frame_id):
			self.mem[frame_id][1] = 1 # set the referenced bit
			
			if mode:
				self.mem[frame_id][0] = "data2"
				self.mem[frame_id][2] = 1 # set the modified bit
				return None
			else:
				self.mem[frame_id][2] = 0 # set the modified bit
				return self.mem[frame_id][0]
		return None

	def evict():
		if len(self.mem) == self.s:
			class1 = get_all(0,0)
			if len(class1) > 0:
				del self.mem[random.choice(class1)]
				return

			class2 = get_all(0,1)
			if len(class2) > 0:
				del self.mem[random.choice(class1)]
				return

			class3 = get_all(1,0)
			if len(class3) > 0:
				del self.mem[random.choice(class1)]
				return

			class4 = get_all(1,1)
			if len(class4) > 0:
				del self.mem[random.choice(class1)]
				return

	def get_all(ref, mod):
		return [i for i in self.mem if self.mem[i][1:] == (ref,mod)]
