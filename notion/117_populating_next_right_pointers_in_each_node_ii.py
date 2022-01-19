"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        level = [root] 
        while(level):
            curr_lvl = level
            level = []
            for idx in range(len(curr_lvl)):
                node = curr_lvl[idx]
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
                if idx < len(curr_lvl) - 1:
                    node.next = curr_lvl[idx + 1]
        return root