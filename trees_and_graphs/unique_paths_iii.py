class Solution(object):
    def __init__(self):
        self.max_empty_squares = 0
        self.start_square = (0, 0)
        self.max_row = 0
        self.max_col = 0

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.finding_info()

    def finding_info(self):
        self.max_row = max(self.grid)
        self.max_col = max(self.grid[0])
        for row in range(self.grid):
            for col in range(self.grid[row]):
                if self.grid[row][col] == 0:
                    self.max_empty_squares += 1
                if self.grid[row][col] == 1:
                    self.start_square = (row, col)

    def dfs(self):
        path = []
        stack = []
        visited = []
        current = self.start_square
        while stack or current:
            row, col = current
            left_neighbor = self.get_neighbors((row, col - 1))
            right_neighbor = self.get_neighbors((row, col + 1))
            up_neighbor = self.get_neighbors((row - 1, col))
            down_neighbor = self.get_neighbors((row + 1, col))
    
    def get_neighbors(self, coord):
        neighbor = self.check_neighbor(coord)
        if neighbor:
            return coord
    
    def check_neighbor(self, coord):
        row, col = coord
        if row >= self.max_row or row < 0:
            return False
        if col >= self.max_col or col < 0:
            return False
        if self.grid[row][col] == -1:
            return False
        if self.grid[row][col] == 2:
            return False
        if self.grid[row][col] == 0:
            return coord
   
    
