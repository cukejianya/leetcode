# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        return self.reverseListRecur(head)[0]

    def reverseListRecur(self, head):
        if head.next == None:
            return (head, None)
        (new_head, tail) = self.reverseListRecur(head.next)
        if tail:
            tail.next = head
        else:
            new_head.next = head
        
        tail = head
        tail.next = None

        return (new_head, tail)

    def reverseListIter(self, head):
        curr = head
        head = None
        while curr != None:
            next_node = curr.next
            curr.next = head
            head = curr
            curr = next_node
        
        return head
            
