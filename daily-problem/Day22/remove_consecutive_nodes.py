class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def removeConsecutiveSumTo0(node):
  index_rem = {}
  sums= []

  # Check the nodes we need to remove
  current_node = node
  while current_node:
    len_sums = len(sums)
    for i in range(len_sums):
      if sums[i] + current_node.value == 0:
        index_rem[i] = len_sums
      sums[i] += current_node.value
    sums.append(current_node.value)
    current_node = current_node.next
  
  # Remove the nodes
  index_node = 0
  index_remove = 0
  start_rem_index = list(index_rem.keys())
  current_node = node
  last_node = None
  while current_node:
    index_start = start_rem_index[index_remove]
    while index_start < index_node and index_remove < len(start_rem_index):
      index_start = start_rem_index[index_remove]
      index_remove += 1
    
    if index_node == index_start - 1:
      last_node = current_node

    if index_node == index_start:
      while index_node < index_rem[index_start] + 1:
        current_node = current_node.next
        index_node += 1
      if last_node == None:
        node = current_node
      else:
        last_node.next = current_node
      index_remove += 1
    else:
      current_node = current_node.next
      index_node += 1

  return node

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)

while node:
  print(node.value)
  node = node.next
# 10
