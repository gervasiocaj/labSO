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
    self.mem[frame_id] = ("data1", 0)

  def access(self, frame_id, mode):
    if mode:
      if not contains(frame_id):
        q.insert(0, frame_id)
      self.mem[frame_id] = ("data2", 0)
      return
    else:
      self.mem[frame_id][1] = 1
      return self.mem[frame_id][0]

  def evict(self):
    f_id = q.pop()
    if self.mem[f_id][1] == 1:
      

    del self.mem[]
