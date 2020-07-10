'''
You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
'''
def matrix_spiral_print(M):
    start_pos = 0
    max_row = len(M)
    max_column = len(M[0])
    times_run_row = max_row // 2 + max_row % 2
    times_run_col = max_column // 2 + max_column % 2
    run_circle = 0
    spiral_list = []

    while run_circle < times_run_row and run_circle < times_run_col:

        # First for will go to the top left to the top right
        for j in range(start_pos, max_column):
            spiral_list.append(M[start_pos][j])

        # Second for will go to the top right to the bot right
        for j in range(start_pos + 1, max_row):
            spiral_list.append(M[j][max_column - 1])

        if max_row > 1:
            for j in range(max_column - 2, start_pos - 1, -1):
                spiral_list.append(M[max_row - 1][j])

        if max_column > 1:
            for j in range(max_row - 2, start_pos, -1):
                spiral_list.append(M[j][start_pos])

        max_row -= 1
        max_column -= 1
        start_pos += 1
        run_circle += 1

    spiral_len = len(spiral_list)

    for i in range(spiral_len):
        if i < spiral_len - 1:
            print("%d," % spiral_list[i]),
        else:
            print(spiral_list[i]),


grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
