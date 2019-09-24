class Solution():
    def floodFill(self, image, sr, sc, newColor):
        color = image[sr][sc]
        queue = [(sr, sc)]
        visited = set(queue)
        row_len = len(image)
        col_len = len(image[0])
        while(queue):
            x, y = queue.pop(0)
            image[x][y] = newColor
            cell = (x - 1, y) 
            if x > 0 and image[x - 1][y] == color and cell not in visited:
                queue.append(cell)
                visited.add(cell)
            cell = (x + 1, y) 
            if x < row_len - 1 and image[x + 1][y] == color and cell not in visited:
                queue.append(cell)
                visited.add(cell)
            cell = (x, y - 1) 
            if y > 0 and image[x][y - 1] == color and cell not in visited:
                queue.append(cell)
                visited.add(cell)
            cell = (x, y + 1) 
            if y < col_len - 1 and image[x][y + 1] == color and cell not in visited:
                queue.append(cell)
                visited.add(cell)
        return image