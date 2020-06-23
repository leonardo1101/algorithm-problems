def findPythagoreanTriplets(nums):
  nums.sort()
  nums_size = len(nums)
  result = 0

  for i in range(nums_size):
    nums[i] *= nums[i]

  for k in range(nums_size - 1, -1, -1):
    result = nums[k]
    i = 0
    j = k
    while i < j:
      if nums[i] + nums[j] == result:
        return True
      elif nums[i] + nums[j] < result:
        i += 1
      else:
        j -= 1
  return False

print findPythagoreanTriplets([3, 12, 5, 13])
