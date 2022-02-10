# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            curr, lvl = queue.pop(0)
            if not curr.left and not curr.right:
                return lvl
            if curr.left:
                queue.append((curr.left, lvl + 1))
            if curr.right:
                queue.append((curr.right, lvl + 1))
