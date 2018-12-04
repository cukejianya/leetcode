class Solution:
    def __init__(self):
        self.visited = set([])
        self.board = []
        self.row_len = 0
        self.col_len = 0

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row_len = len(board)
        if not self.row_len:
            return None
        self.col_len = len(board[0])
        for row in range(self.row_len):
            if (row, 0) not in self.visited and self.board[row][0] == 'O':
                self.find_region((row, 0))
            if (row, self.col_len - 1) not in self.visited and self.board[row][self.col_len - 1] == 'O':
                self.find_region((row, self.col_len - 1))
        for col in range(self.col_len):
            if (0, col) not in self.visited and self.board[0][col] == 'O':
                self.find_region((0, col))
            if (self.row_len - 1, col) not in self.visited and self.board[self.row_len - 1][col] == 'O':
                self.find_region((self.row_len - 1, col))
        for row in range(self.row_len):
            for col in range(self.col_len):
                if self.board[row][col] == 'O' and (row, col) not in self.visited:
                    self.board[row][col] = 'X'

    def find_region(self, coord):
        self.visited.add(coord)
        stack = []
        current = coord
        while(current or stack):
            if current:
                neighbors = self.get_neighbors(current)
                if neighbors:
                    self.visited.update(neighbors)
                    current = neighbors.pop()
                    stack.extend(neighbors)
                else:
                    current = None
            else:
                current = stack.pop()

    def get_neighbors(self, coord):
        row, col = coord
        neighbors = []
        new_row = row - 1
        if not new_row < 0 and (new_row, col) not in self.visited:
            if self.board[new_row][col] == 'O':
                neighbors.append((new_row, col))
        new_row = row + 1
        if not new_row > self.row_len - 1 and (new_row, col) not in self.visited:
            if self.board[new_row][col] == 'O':
                neighbors.append((new_row, col))
        new_col = col - 1
        if not new_col < 0 and (row, new_col) not in self.visited:
            if self.board[row][new_col] == 'O':
                neighbors.append((row, new_col))
        new_col = col + 1
        if not new_col > self.col_len - 1 and (row, new_col) not in self.visited:
            if self.board[row][new_col] == 'O':
                neighbors.append((row, new_col))
        return neighbors