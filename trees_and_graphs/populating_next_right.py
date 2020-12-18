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
        stack = [(root, 0)]
        while stack and root:
            curr, lvl = stack.pop(0)
            if stack:
                nxt_node, nxt_lvl = stack[0]
                curr.next = nxt_node if nxt_lvl == lvl else None
            if curr.left:
                stack.append((curr.left, lvl + 1))
            if curr.right:
                stack.append((curr.right, lvl + 1))
        return root
