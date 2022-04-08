# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.dfs(root, []) 
        return self.max

    def dfs(self, node, ancestors):
        for val in ancestors:
            self.max = max(self.max, abs(val - node.val))
        ancestors.append(node.val)
        if node.left:
            self.dfs(node.left, ancestors[::])
        if node.right:
            self.dfs(node.right, ancestors[::])



