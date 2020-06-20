class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print self.value,
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invert(node):
  stack = []
  stack.append(node) 
  while stack:
    current_node = stack.pop()
    aux_node = None
    if current_node:
      stack.append(current_node.right)
      stack.append(current_node.left)
      aux_node = current_node.left 
      current_node.left = current_node.right
      current_node.right = aux_node


root = Node('a') 
root.left = Node('b') 
root.right = Node('c') 
root.left.left = Node('d') 
root.left.right = Node('e') 
root.right.left = Node('f') 

root.preorder()
# a b d e c f 
print "\n"
invert(root)
root.preorder()
# a c f b e d
