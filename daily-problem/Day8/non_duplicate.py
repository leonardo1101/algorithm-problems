def singleNumber(nums):
  nums_len = len(nums)
  sum_nums = 0
  for index in range(nums_len):
    if sum_nums - nums[index] < 0:
        sum_nums += nums[index]
    else:
        sum_nums -= nums[index]
  return sum_nums

print singleNumber([4, 3, 2, 1, 4, 11, 1, 3, 2])
# 1
