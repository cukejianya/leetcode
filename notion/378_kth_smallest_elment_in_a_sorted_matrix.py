import math 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        total = len(matrix) ** 2
        corner_idx = math.floor(math.sqrt(k))
        distance = math.ceil((total - k) //2)
        if distance == 0:
            return matrix[corner_idx][corner_idx]
        left = matrix[corner_idx - distance][corner_idx]
        up = matrix[corner_idx][corner_idx - distance]
        if (total - k) % 2:
            return max(left, up)
        return min(left, up)


