class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        buildings = []
        for row in grid:
            for col in grid[0]:
                buildings.append((row, col))
        for idx in len(buildings):
            queue = [buildings[idx]]
            level = 0
            while(queue):
                seen = set()
                curr_queue = queue
                queue = []
                for row, col in curr_queue:
                    if not grid:
                        grid[row][col] = {
                            total: 0
                            count: 0
                        }
                        
                    up = (row - 1, col)
                    down = (row + 1, col)
                    left = (row, col - 1)
                    right = (row, col + 1)
                    if row > 0 and grid[row - 1][col] not in [1, 2] and up not
                    in seen:
                        queue.append(up) 
                    if row < len(grid) and grid[row + 1][col] not in [1, 2] and
                    down not in seen:
                        queue.append(down) 
                    if col > 0 and grid[row][col - 1] not in [1, 2] and left not
                    in seen:
                        queue.append(left) 
                    if col < len(grid) and grid[row][col + 1] not in [1, 2] and
                    right not in seen:
                        queue.append(right) 
