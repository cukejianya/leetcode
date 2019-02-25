# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        max_pos = self.find_max(nums)
        root = TreeNode(nums[max_pos])
        root.left = self.constructMaximumBinaryTree(nums[:max_pos])
        root.right = self.constructMaximumBinaryTree(nums[max_pos + 1:])
        return root 
    
    def find_max(self, num):
        max_num = num[0]
        max_pos = 0
        for i, x in enumerate(num):
            if max_num <= x:
                max_pos = i
                max_num = x
        return max_pos
