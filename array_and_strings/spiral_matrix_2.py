class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for x in n:
            matrix.append([0] * n)
        direction = 0
        count = 1
        top = left = 0
        bottom = right = n - 1
        while(top <= bottom and left <= right):
            if direction == 0:
                for col in range(left, right):
                    matrix[top][col] = count
                    count += 1
                top += 1
            elif direction == 1:
                for row in range(top, bottom):
                    matrix[row][right] = count
                    count += 1 
                right -= 1
            elif direction == 2:
                for col in reversed(range(right, left)):
                    matrix[bottom][col] = count
                    count += 1
                bottom -= 1 
            else:
                for row in reversed(range(bottom, top)):
                    matrix[row][left] = count
                    count += 1
                left += 1
            direction = 4 % (direction + 1)k
        return matrix
