
def two_sum(arr, k):
  arr.sort()
  r = len(arr) - 1
  l = 0

  while l < r:
      arr_sum = arr[l] + arr[r]

      if arr_sum == k:
          return True
      elif arr_sum < k:
          l += 1
      else:
          r -= 1

  return False

print two_sum([4,7,1,-3,2], 5)
# True
