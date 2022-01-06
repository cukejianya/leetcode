# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        while(stack):
            curr_node = stack[-1]
            if curr_node.left

        pass

    def dfs(self, node, prev_val):




