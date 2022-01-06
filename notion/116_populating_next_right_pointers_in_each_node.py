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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        curr_lvl = [root]
        while curr_lvl:
            next_lvl = []
            curr_lvl_count = len(curr_lvl)
            for i in range(curr_lvl_count):
                curr_node = curr_lvl[i]
                if curr_node.left:
                    next_lvl.append(curr_node.left)
                if curr_node.right:
                    next_lvl.append(curr_node.right)
                if i < curr_lvl_count - 1:
                    curr_node.next = curr_lvl[i + 1]
            curr_lvl = next_lvl
        return root
