from nru import PhysicalMemory as nru
from aging import PhysicalMemory as ag
from fifo import PhysicalMemory as fifo
from second_chance import PhysicalMemory as sc

class PhysicalMemory:
  def __init__(self, algorithm):
    x = {"fifo": fifo, "nru": nru, "aging": ag, "second-chance": sc}
    self.xpto = x[algorithm]()

  def put(self, frameId):
    self.xpto.put(frameId)

  def evict(self):
    return self.xpto.evict()

  def clock(self):
    self.xpto.clock()

  def access(self, frameId, isWrite):
    return self.xpto.access(frameId, isWrite)
