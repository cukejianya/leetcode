# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []        
        curr_node = head
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.next
        curr_node = head
        if len(stack) < 2:
            return head
        while curr_node != stack[-1]:
            next_node = curr_node.next
            if next_node == stack[-1]:
                break
            stack[-1].next = next_node
            curr_node.next = stack.pop()
            curr_node = next_node
        next_node.next = None
        return head
