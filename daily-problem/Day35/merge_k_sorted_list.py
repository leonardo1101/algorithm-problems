'''
Merge K Sorted Linked Lists

You are given an array of k sorted singly linked lists. Merge the linked lists
into a single sorted linked list and return it.
'''

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    merge_list = []
    current_node_a = lists[0]
    current_node_b = lists[1]
    while current_node_a != None or current_node_b != None:
        if current_node_a == None:
            merge_list.append(current_node_b.val)
            current_node_b = current_node_b.next
        elif current_node_b == None:
            merge_list.append(current_node_a.val)
            current_node_a = current_node_a.next
        elif current_node_a.val < current_node_b.val:
            merge_list.append(current_node_a.val)
            current_node_a = current_node_a.next
        else:
            merge_list.append(current_node_b.val)
            current_node_b = current_node_b.next
    return merge_list

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print merge([a, b])
# 123456
