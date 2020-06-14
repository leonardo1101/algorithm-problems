class Solution:
  def binarySearchFirst(self, arr, x):
    index = 0
    r = len(arr)
    l = 0
    while True:
      while l <= r:
        index = l + (r - l)//2
        if arr[index] == x:
          break 
        elif arr[index] < x:
          l = index + 1
        else:
          r = index - 1

      if r < l :
        return -1

      if index == 0:
        return 0
      else:
        if arr[index - 1] != x:
          return index
        else:
          r = index - 1

  def binarySearchLast(self, arr, x):
    index = 0
    r = len(arr)
    l = 0
    while True:
      while l <= r:
        index = l + (r - l)//2
        if arr[index] == x:
          break 
        elif arr[index] < x:
          l = index + 1
        else:
          r = index - 1

      if r < l :
        return -1

      if index == len(arr) - 1:
        return index
      else:
        if arr[index + 1] != x:
          return index
        else:
          l = index + 1

    pass
  def getRange(self, arr, target):
    res = []
    first = Solution().binarySearchFirst(arr, target)
    if first == -1:
        res.append(-1)
        res.append(-1)
    else:
        last = Solution().binarySearchLast(arr, target)
        res.append(first)
        res.append(last)
    return res

# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
print(Solution().getRange(arr, x))
# [1, 4]
