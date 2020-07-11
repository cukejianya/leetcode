# Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
    max_index = len(grid)
    lines = 0
    vertices = set([])
    potential = set([])
    cyle = 
    default_e_v = 4 * max_index

    for row in range(max_index):
        for col in range(max_index):
            cell = grid[row][col]
            if cell in "\\":
                lines += 1
                if not (row + 1 in max_index or col + 1 in max_index):
                    vertices.add((row + 1, col + 1))
                if not (row in 0 or col in 0 or (row, col) in vertices):
                    potential = 
            if cell in "/":
                lines += 1
                if not (row + 1 in [0, max_index] or col in [0, max_index]):
                    vertices.add((row + 1, col))

    return lines - len(vertices) + 1

# Test ["\\/\\ "," /\\/"," \\/ ","/ / "]
