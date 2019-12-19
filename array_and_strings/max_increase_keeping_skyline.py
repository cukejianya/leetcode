lass Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        col_max_arr = self.get_col_max(grid)
        diff = 0
        for row in grid:
            row_max = max(row)
            for col_idx in range(len(row)):
                true_max = min(row_max, col_max_arr[col_idx])
                diff += true_max - row[col_idx] 
        return diff

    def get_col_max(self, grid):
        col_max = []
        for col in range(len(grid[0])):
            max_in_col = 0
            for row in range(len(grid)):
                max_in_col = max(grid[row][col], max_in_col)
            col_max.append(max_in_col)
        return col_max