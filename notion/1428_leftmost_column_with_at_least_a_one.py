# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        leftMost_pos = float('inf')
        dimensions = binaryMatrix.dimensions()
        max_row = dimensions[0]
        max_col = dimensions[1]
        for row in range(max_row):
            left_col = 0
            right_col = max_col - 1
            if binaryMatrix.get(row, right_col) == 1:
                mid_col = (right_col + left_col) // 2
                while(left_col != right_col):
                    cell = binaryMatrix.get(row, mid_col)
                    if cell == 0:
                        left_col = mid_col + 1
                    if cell == 1:
                        right_col = mid_col
                leftMost_pos = min(leftMost_pos, mid_col)
        return leftMost_pos if leftMost_pos != float('inf') else -1
