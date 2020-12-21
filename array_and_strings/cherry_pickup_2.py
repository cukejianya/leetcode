class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.max_level = len(grid)
        self.max_moves = len(grid[0])
        self.grid = grid
        self.save = {}

    def bfs(self, lvl, rob_1, rob_2, cherries):
        cherries += self.grid[lvl][rob_1] + self.grid[lvl][rob_2]
        if lvl == (self.max_level - 1):
            return cherries

        max_chrs = 0
        for m1 in (rob_1 - 1, rob_1, rob_1 + 1):
            for m2 in (rob_2 - 1, rob_2, rob_2 + 1):
                if (lvl + 1, m1, m2) in self.save:
                   max_chrs = max(max_chrs, self.save[lvl + 1, m1, m2]) 
                elif m1 >= m2 or m1 < 0 or m2 >= self.max_moves:
                    max_chrs = max(max_chrs, self.bfs(lvl + 1, m1, m2, cherries))

        self.save[(lvl, rob_1, rob_2)] = max_chrs 
        return max_chrs 
