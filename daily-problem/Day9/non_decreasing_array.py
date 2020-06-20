def check(lst):
  number_peak = 0
  len_lst = len(lst)

  for i in range(1, len_lst):
    if lst[i - 1] > lst[i]:
      number_peak += 1
      if number_peak > 1:
          return False
  return True


print check([13, 4, 7])
# True
print check([5,1,3,2,5])
# False
