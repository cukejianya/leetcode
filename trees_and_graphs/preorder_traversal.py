# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        retList = []
        while(stack):
            curr = stack.pop()
            retList.append(curr.val)
            if (curr.right):
                stack.append(curr.right)
            if (curr.left):
                stack.append(curr.left)
        return retList