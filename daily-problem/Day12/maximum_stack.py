class MaxStack:
  def __init__(self):
    self.stack = []
    self.max_stack = [None]
    self.current_max = None

  def push(self, val):
    self.stack.append(val)
    if self.current_max == None or self.current_max < val:
      self.current_max = val
    self.max_stack.append(self.current_max)

  def pop(self):
    self.max_stack.pop()
    self.current_max = self.max_stack.pop()
    self.max_stack.append(self.current_max)
    return self.stack.pop()

  def max(self):
    return self.current_max

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print s.max()
s.pop()
s.pop()
print s.max()
