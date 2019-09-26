class Solution:
    def updateMatrix(self, matrix):
        queue = []
        self.row_len = len(matrix)
        self.col_len = len(matrix[0])
        for x in range(self.row_len):
            for y in range(self.col_len):
                if matrix[x][y] == 0:
                    queue.append((x, y))
                else:
                    matrix[x][y] = 10001
        visited = set(queue)
        while(queue):
            x, y = queue.pop(0)
            if x > 0:
                self.handle_cell(matrix, queue, visited, (x - 1, y),
                                 matrix[x][y] + 1)    
            if y > 0:
                self.handle_cell(matrix, queue, visited, (x, y - 1),
                                 matrix[x][y] + 1)    
            if x < self.row_len - 1:
                self.handle_cell(matrix, queue, visited, (x + 1, y),
                                 matrix[x][y] + 1)    
            if y < self.col_len - 1:
                self.handle_cell(matrix, queue, visited, (x, y + 1),
                                 matrix[x][y] + 1)    
        return matrix

    def handle_cell(self, matrix, queue, visited, cell, level):
        x, y = cell
        if cell not in visited:
            visited.add(cell)
            dist = matrix[x][y]
            if dist > level:
                queue.append((x, y))
                visited.add((x, y))
                matrix[x][y] = level