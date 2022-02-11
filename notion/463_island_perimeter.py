class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        stack = [] 
        seen = set()
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    stack.append((row, col))
                    break
            if grid[row][col]:
                break
        while stack:
            row, col = stack.pop()
            for x, y in direction:
                if row + x > 0 and row + x < len(grid) and col + y > 0 and col
                + y < len(grid[0]) and grid[row + x][col + y] == 1 and not
                (row + x, col + y) in seen:
                    stack.append((row + x, col + y))
                    seen.add((row + x, col + y)) 
                elif (row + x, col + y) not in seen:
                    perimeter += 1
        return perimeter
