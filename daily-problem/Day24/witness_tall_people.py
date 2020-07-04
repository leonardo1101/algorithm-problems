def witnesses(heights):
  max = 0
  count_witnesses = 0
  number_people = len(heights)

  for i in range(number_people - 1,-1, - 1):
    if heights[i] > max:
      count_witnesses += 1
      max = heights[i]
  return count_witnesses 
print(witnesses([3, 6, 3, 4, 1]))
# 3