class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    buildings.append((row,col))

        minimal_distance = float('inf')
        for home in buildings:
            queue = [home]
            seen = set()
            level = 0
            while(queue):
                row, col = queue.pop(0)
                seen.add((row, col))
                if grid[row][col] % 3 == 0:
                    grid[row][col] += 3*level
                    minimal_distance = min(minimal_distance, grid[row][col]) 
                up = (row - 1, col)
                down = (row + 1, col)
                left = (row, col - 1)
                right = (row, col + 1)
                if row > 0 and up not in seen and grid[up[0]][up[1]] % 3:
                    queue.append(up)
            
                if row < len(grid) and down not in seen and grid[down[0]][down[1]] % 3:
                    queue.append(down)

                if row < len(grid[0]) and left not in seen and grid[left[0]][left[1]] % 3:
                    queue.append(left)

                if row < len(grid[0]) and right not in seen and grid[right[0]][right[1]] % 3:
                    queue.append(right)
        return minimal_distance
    
    def getDistance(self, pt_1, pt_2):
        return abs(pt_1[0] - pt_2[0]) + abs(pt_1[1] - pt[2])
