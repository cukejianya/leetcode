def spiralOrder(self, matrix):
    solution = []
    if not len(matrix):
        return solution
    row_limit = len(matrix)
    col_limit = len(matrix[0])
    row_start = 0
    col_start = 0
    sign = 1
    while(row_limit and col_limit):
        row_limit = row_limit - 1
        for i in range(col_start, col_start + (sign * col_limit), sign):
            solution.append(matrix[row_start][i])
            col_start = i
        row_start = row_start + sign
        for i in range(row_start, row_start + (sign * row_limit), sign):
            solution.append(matrix[i][col_start])
            row_start = i
        col_limit = col_limit - 1
        sign = sign * -1
        col_start = col_start + sign
    return solution
