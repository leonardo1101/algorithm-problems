class Stack :
  def __init__(self) :
    self.items = []
    self.len = 0

  def push(self, item) :
    self.items.append(item)
    self.len += 1

  def pop(self) :
    self.len -= 1
    return self.items.pop()

  def top(self):
    return self.items[self.len - 1]

  def isEmpty(self) :
    return (self.items == [])

class Solution:
  def isValid(self, s):
    stack = Stack()
    index = 0
    match = { "{": "}", "[": "]", "(": ")"}

    for index in range(len(s)):
        if stack.isEmpty() or s[index] in match.keys():
            stack.push(s[index])
        else:
            if match[stack.top()] == s[index]:
                stack.pop()
            else:
                return False

    if stack.isEmpty():
        return True
    else:
        return False


# Test Program
s = "()(){(())"
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))

