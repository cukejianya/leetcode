# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def dfs(node):
            if not node:
                return 0
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            self.max_diameter = max(right_len + left_len, self.max_diameter)
            return max(right_len, left_len) + 1
        dfs(root)
        return self.max_diameter
