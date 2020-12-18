# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ptr = TreeNode(None) 
        curr = ptr 
        stack = [root]
        while(stack):
            while(root.left):
                stack.append(root.left)
                root = root.left
            root = stack.pop()
            root.left = None
            curr.right = root
            curr = root
            if root.right:
                stack.append(root.right) 
                root = root.right
        return ptr.right 

    def dfs(self, root):
        if root:
            self.dfs(root.left)
            if not self.head:
                self.head = root
                self.curr = root
            else:
                root.left = None
                self.curr.right = root
                self.curr = root
            self.dfs(root.right)
