"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        if not self.nodesMapping:
            self.nodesMapping = {}
        new_head = Node(head.val) 
        if head.random in self.nodesMapping:
            new_head.random = self.nodesMapping[head.random]
        self.nodesMapping[head] = new_head
        new_head.next = self.copyRandomList(head.next)
        return new_head
