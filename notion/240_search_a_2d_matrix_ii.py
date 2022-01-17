class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left, col_left = 0
        row_right = len(matrix)
        col_right = len(matrix[0])
        while row_left < row_right - 1:
            row_mid = (row_left + row_right) // 2
            while col_left < col_right - 1:
                col_mid = (col_left + col_right) // 2
                if target < matrix[row_mid][col_mid]:
                    col_right = col_mid
                else:
                    col_left = col_mid
            if target < matrix[row_mid][col_left]:
                row_right = row_mid
            else:
                row_left = row_mid
        return matrix[row_left][col_left] == target

