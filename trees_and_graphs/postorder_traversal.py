# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        visited = set([None])
        values = []
        while(stack):
            curr = stack.pop()
            if curr.left in visited and curr.right in visited:
                values.append(curr.val)
            if curr.left not in visited:
                stack.append(curr)
                stack.append(curr.left)
                visited.add(curr.left)
            elif curr.right not in visited:
                stack.append(curr)
                stack.append(curr.right)
                visited.add(curr.right)
        return values