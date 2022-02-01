# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    seen = set()
    while(headB or headA):
        if headA in seen:
            return headA.val
        if headA:
            seen.add(headA)
            headA = headA.next
        if headB in seen:
            return headB.val
        if headB:
            seen.add(headB)
            headB = headB.next
    return None
