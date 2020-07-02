def num_ways(n, m):
  matrix = []

  for i in range(n):
    row = [0] * m
    matrix.append(row)

  matrix[0][0] = 1

  for i in range(n):
    for j in range(m):
      if j < m - 1:
        matrix[i][j + 1] += 1
      if i < n - 1:
        matrix[i + 1][j] += 1

  return matrix[n - 1][m - 1]

print num_ways(2, 2)
# 2
