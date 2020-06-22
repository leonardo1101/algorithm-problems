def staircase(n):
  max_steps = 2
  stairs = n
  dp_matrix = []
  for number_stair in range(n + 1):
    ways_climb = []
    for number_step in range(max_steps + 1):
      if number_stair == 0 or number_step == 0:
        ways_climb.append(0)
      elif number_step == 1:
        ways_climb.append(1)
      else:
        if number_stair >= 2:
          possible_ways = number_stair//2 + ways_climb[number_step - 1] + dp_matrix[number_stair - number_step][number_step]
          ways_climb.append(possible_ways)
        else:
          ways_climb.append(ways_climb[number_step - 1])
    dp_matrix.append(ways_climb)
  return dp_matrix[n][max_steps]
print staircase(4)
# 5
print staircase(5)
# 8
