# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        if root is None:
            return 0
        
        total = 0
        if root.val >= L and root.val <= R:
            total = root.val
        if root.val > L:
            total += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            total += self.rangeSumBST(root.right, L, R)

        return  total