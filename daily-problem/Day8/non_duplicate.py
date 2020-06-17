def singleNumber(nums):
  nums_len = len(nums)
  sum_pos_pair = 0
  sum_pos_odd = 0
  sum_neg_pair = 0
  sum_neg_odd = 0
  for index in range(nums_len):
    if nums[index] > 0:
      if nums[index] % 2:
        sum_pos_odd += nums[index]
      else:
        sum_pos_pair += nums[index]
    else:
      if abs(nums[index]) % 2:
        sum_neg_odd += nums[index]
      else:
        sum_neg_pair += nums[index]
  
  if sum_pos_odd % 2 != 0:
    return sum_pos_odd % 2
  elif sum_pos_pair % 4 != 0:
    return sum_pos_pair % 4
  elif sum_neg_odd % 2 != 0:
    return -(sum_neg_odd % 2)
  elif sum_neg_pair % 4 != 0:
    return -(sum_neg_pair % 4)
  else:
    return 0

print singleNumber([4, 3, 2, 1, 4, -2, 1, 3, 2])

