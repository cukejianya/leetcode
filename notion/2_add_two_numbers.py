# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr_node1 = l1
        curr_node2 = l2
        prev_node = None
        while curr_node1 and curr_node2:
            curr_node1.val += (curr_node2.val + carry)
            carry = curr_node1.val // 10
            curr_node1.val %= 10
            prev_node = curr_node1
            curr_node1 = curr_node1.next
            curr_node2 = curr_node2.next
        if curr_node2:
            prev_node.next = curr_node2
            curr_node1 = curr_node2
        while curr_node1 and carry:
            curr_node1 += carry
            carry = curr_node1.val // 10
            curr_node1.val %= 10
            curr_node1 = curr_node1.next
        return l1
