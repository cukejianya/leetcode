# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = [root]
        found_null = False
        while queue:
            level = queue
            children_level = []
            for node in level:
                if node != None and found_null:
                    return False
                if node == None:
                    found_null = True
                else:
                    children_level.append(node.left) 
                    children_level.append(node.right)
            queue = children_level
        return True