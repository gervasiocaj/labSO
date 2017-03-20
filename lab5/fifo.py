import random

class PhysicalMemory:
	def __init__(self):
		self.mem = {}
		self.q = []

	def clock(self):
		pass

	def contains(self, frame_id):
		return frame_id in self.mem

	def put(self, frame_id):
		q.insert(0, frame_id)
		self.mem[frame_id] = "data1" 

	def access(self, frame_id, mode):
		if mode:
			if not contains(frame_id):
				q.insert(0, frame_id)
			self.mem[frame_id] = "data2"
			return
		else:
			return self.mem[frame_id]

	def evict(self):
		if len(q) > 0:
			del self.mem[q.pop()]
