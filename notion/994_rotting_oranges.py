class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        rotten  = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col] 
                if cell != 0:
                    count += 1
                if cell == 2:
                    rotten.append((row, col, 0))
        min_rotten = 0
        seen = set()
        while rotten:
            row, col, level = rotten.pop(0)
            min_rotten = max(min_rotten, level)
            count -= 1
            up = (row - 1, col, level + 1)
            down = (row + 1, col, level + 1)
            left = (row, col - 1, level + 1)
            right = (row, col + 1, level + 1)
            if row > 0 and not (up[0], up[1]) in seen and grid[up[0]][up[1]] == 1:
                rotten.append(up)
                seen.add((up[0], up[1]))
            if row < len(grid) - 1 and not (down[0], down[1]) in seen and grid[down[0]][down[1]] == 1:
                rotten.append(down)
                seen.add((down[0], down[1]))
            if col > 0 and not (left[0], left[1]) in seen and grid[left[0]][left[1]] == 1:
                rotten.append(left)
                seen.add((left[0], left[1]))
            if col < len(grid[0]) - 1 and not (right[0], right[1]) in seen and grid[right[0]][right[1]] == 1:
                rotten.append(right)
                seen.add((right[0], right[1]))
        if count != 0:
            return -1
        return min_rotten
