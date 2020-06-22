def staircase(n):
  # Max steps that we can make
  max_steps = 2
  stairs = n
  # Table to hold the old ane new values
  dp_matrix = []
  # We will calculate the unique ways for 0 until n
  for number_stair in range(n + 1):
    ways_climb = []
    # Check for each step until 2
    for number_step in range(max_steps + 1):
      # The default value will be 1
      if number_stair == 0 or number_step == 0:
        ways_climb.append(1)
      # If the step is one we will subtract one and get the maximum ways for the last case
      elif number_step == 1:
        ways_climb.append(dp_matrix[number_stair - number_step][max_steps])
      else:
        # If the step is two we will get the ways with one step plus the maximum ways
        # for the current number of stairs minus 2
        if number_stair >= 2:
          possible_ways = ways_climb[number_step - 1] + dp_matrix[number_stair - number_step][max_steps]
          ways_climb.append(possible_ways)
        else:
          ways_climb.append(ways_climb[number_step - 1])

    dp_matrix.append(ways_climb)
  return dp_matrix[n][max_steps]
print staircase(4)
# 5
print staircase(5)
# 8
