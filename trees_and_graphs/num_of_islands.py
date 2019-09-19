class Solution:
    def traverse_island(self, grid, cell):
        row_max = len(grid)
        col_max = len(grid[0])
        will_visit = [cell]
        grid[cell[0]][cell[1]] = "0"
        while will_visit:
            cell = will_visit.pop(0)
            x, y = cell
            if x > 0 and grid[x - 1][y] == "1":
                will_visit.append((x - 1, y))
                grid[x - 1][y] = "0"
            if x + 1 < row_max and grid[x + 1][y] == "1":
                will_visit.append((x + 1, y))
                grid[x + 1][y] = "0"
            if y > 0 and grid[x][y - 1] == "1":
                will_visit.append((x, y - 1))
                grid[x][y - 1] = "0"
            if y + 1 < col_max and grid[x][y + 1] == "1":
                will_visit.append((x, y + 1))
                grid[x][y + 1] = "0"
        return 1

    def numIslands(self, grid):
        num_of_islands = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    num_of_islands += self.traverse_island(grid, (x,y))
        return num_of_islands