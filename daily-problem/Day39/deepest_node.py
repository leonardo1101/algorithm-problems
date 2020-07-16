'''
Deepest Node in a Binary Tree

You are given the root of a binary tree. Return the deepest node (the furthest
node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.
'''
class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __repr__(self):
    return self.val


def deepest(node):
    list_nodes = []
    current_level = 1
    list_nodes.append(node)
    max_level = 0
    res = None

    while list_nodes:
        new_list = []
        num_nodes = len(list_nodes)
        for i in range(num_nodes):
            current_node = list_nodes[i]
            if not current_node.left and not current_node.right:
                if current_level > max_level:
                    res = (current_node.val, current_level)
            else:
                if current_node.left:
                    new_list.append(current_node.left)
                if current_node.right:
                    new_list.append(current_node.right)
        list_nodes = new_list
        current_level += 1

    return res

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print deepest(root)
# (d, 3)
