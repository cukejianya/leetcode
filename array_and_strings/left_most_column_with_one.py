class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [row_max, col_max] = binaryMatrix.dimensions()
        left_col = 0
        right_col = col_max - 1
        last_valid_row = 0
        while left_col <= right_col:
            mid_col = (right_col + left_col) // 2
            for row_idx in range(last_valid_row, row_max):
                cell_value = binaryMatrix.get(row_idx, mid_col)
                if cell_value:
                    if left_col == right_col:
                        return mid_col
                    right_col = mid_col
                    last_valid_row = row_idx
                    break
            if not cell_value:
                if left_col == right_col:
                    return -1
                left_col = mid_col + 1