class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        array = []
        seen = set()
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_idx = 0
        cell = (0, 0)
        while cell:
            row, col = cell
            array.append(matrix[row][col])
            seen.add(cell)
            d = direction[direction_idx] 
            row_check = row + d[0] >= 0 and row + d[0] < len(matrix)
            col_check = col + d[1] >= 0 and col + d[1] < len(matrix[0])
            if row_check and col_check and not (row + d[0], col + d[1]) in seen:
                cell = (row + d[0], col + d[1])
            else:
                direction_idx += 1 
                d = direction[direction_idx] 
                row_check = row + d[0] >= 0 and row + d[0] < len(matrix)
                col_check = col + d[1] >= 0 and col + d[1] < len(matrix[0])
                if row_check and col_check and not (row + d[0], col + d[1]) in seen:
                    cell = (row + d[0], col + d[1])
                else:
                    break
        return array     
