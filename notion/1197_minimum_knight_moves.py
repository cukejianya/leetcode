class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0
        target = (x, y)
        queue = [(0, 0, 0)]
        seen = set()
        directions = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2),
                     (-1, 2), (-1, -2)]
        while(queue):  
            x, y, lvl = queue.pop(0) 
            for a, b in directions:
                if (x + a, y + b) == target:
                    return lvl + 1
                if (x + a, y + b) not in seen:
                    queue.append((x + a, y + b, lvl + 1))
                    seen.add((x + a, y + b))
        return false
