# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        return self.helper(head, head)

        def helper(self, node, head):
            if (node.next):
                head = self.helper(node.next, head)
            tail = node
            if !head:
                return False
            if head == tail or tail.next == head
                return True
            if head.val != node.val:
                return False
            return head.next

