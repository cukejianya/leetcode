class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_to_set = set()
        cols_to_set = set()
        row_len = len(matrix)
        col_len = len(matrix[0])
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    rows_to_set.add(row)
                    cols_to_set.add(col)

        for row in range(row_len):
            for col in range(col_len):
                if row in rows_to_set or col in cols_to_set:
                    matrix[row][col] = 0
