class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        if not row_len:
            return
        col_len = len(matrix[0])
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 0:
                    for i in range(row_len):
                        if matrix[i][col] != 0:
                            matrix[i][col] = 'a'
                    for i in range(col_len):
                        if matrix[row][i] != 0:
                            matrix[col][i] = 'a'
        for row in range(row_len):
            for col in range(col_len):
                if matrix[row][col] == 'a':
                    matrix[row][col] = 0

                            
    
        
