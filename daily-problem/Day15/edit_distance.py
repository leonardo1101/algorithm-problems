def distance(s1, s2):
  size_s1 = len(s1) + 1
  size_s2 = len(s2) + 1

  dp_table = []

  # Fill the table with 0
  for i in range(size_s2):
    dp_row = []
    for j in range(size_s1):
      dp_row.append(0)
    dp_table.append(dp_row)


  for i in range(size_s2):
    for j in range(size_s1):
      # Only calculate the distance when there is a character
      if i != 0 and j != 0:
        # If the characters are equal we get the the previous distance
	if s1[j - 1] == s2[i - 1]:
	  dp_table[i][j] = dp_table[i - 1][j - 1]
	else:
          # If the characters aren't equal we get the minor distance and add 1
	  if dp_table[i - 1][j] < dp_table[i][j - 1]:
	    dp_table[i][j] = dp_table[i - 1][j] + 1
	  else:
	    dp_table[i][j] = dp_table[i][j - 1] + 1

  return dp_table[size_s2 - 1][size_s1 - 1]

print distance("biting","sitting")
