def sortNums(nums):
  count_arr = [0, 0, 0]
  res = []
  for index in range(len(nums)):
      num = nums[index]
      count_arr[num - 1] += 1
  
  for number in range(len(count_arr)):
      times_appears = count_arr[number]
      for i in range(times_appears):
          res.append(number + 1)
  return res
print sortNums([3, 3, 2, 1, 3, 2, 1])
# [1, 1, 2, 2, 3, 3, 3]
