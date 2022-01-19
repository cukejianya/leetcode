"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        found_head = None
        curr_node = root
        prev = None
        stack = [root]
        seen = set()
        while stack:
            curr_node = stack[-1]
            if curr_node.left and not curr_node.left in seen:
                stack.append(curr_node.left)
            else:
                curr_node = stack.pop()
                if not found_head:
                    found_head = curr_node
                if prev:
                    curr_node.left = prev
                    prev.right = curr_node
                prev = curr_node
                if curr_node.right and not curr_node.right in seen:
                    stack.append(curr_node.right)
        found_head.left = curr_node
        curr_node.right = found_head

        return found_head

