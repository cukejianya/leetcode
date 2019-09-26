# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        if n == 0:
            return []
        DP = {}
        for start in range(n + 1, 0, -1):
            for end in range(start - 1, n + 1):
                if start > end:
                    DP[(start, end)] = []
                    for i in range(s, e + 1):
                        for l in DP[(i + 1, e)]:
                            node = TreeNode(i)
                            node.left, node.right = l, r
                            DP[(s, e)].append(node)
        return DP[(1, n)]
