class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print c.val,
      c = c.next

def intersection(a, b):
  intersect_left = None
  insersect_right = None
  hashmap = {}

  current_node = a
  while current_node:
    hashmap[current_node.val] = 0
    current_node = current_node.next
  
  current_node = b
  while current_node:
    if current_node.val in hashmap:
      if not intersect_left:
        intersect_left = Node(current_node.val)
        intersect_right = intersect_left
      else:
        intersect_right.next = Node(current_node.val)
        intersect_right = intersect_right.next

    current_node = current_node.next
  return intersect_left

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
# 3 4
