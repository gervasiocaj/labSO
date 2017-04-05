class PhysicalMemory:
	def __init__(self):
		self.mem = {}
		self.q = []

	def clock(self):
		pass

	def contains(self, frame_id):
		return frame_id in self.mem

	def put(self, frame_id):
		self.q.insert(0, frame_id)
		self.mem[frame_id] = "data1" 

	def access(self, frame_id, mode):
		if mode:
			if not self.contains(frame_id):
				self.q.insert(0, frame_id)
			self.mem[frame_id] = "data2"
			return
		else:
			return self.mem[frame_id]

	def evict(self):
		#if len(self.q) > 0:
		f_id = self.q.pop()
		del self.mem[f_id]
		return f_id
