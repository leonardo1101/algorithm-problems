'''
Queue Using Two Stacks

Implement a queue class using two stacks. A queue is a data structure that
supports the FIFO protocol (First in = first out). Your class should support
the enqueue and dequeue methods like a standard queue.
'''

class Queue:
    def __init__(self):
        self.stack_one = []
        self.stack_two = []

    def enqueue(self, val):
        self.stack_one.append(val)

    def dequeue(self):
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())
            if self.stack_two:
                return self.stack_two.pop()
            else:
                return None
        else:
            return self.stack_two.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
print q.dequeue()
# 1 2 3
