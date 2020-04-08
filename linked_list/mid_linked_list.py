class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        middle = head
        idx = 0
        while(head):
            idx += 1
            if (idx % 2 == 0):
                middle = middle.next
            head = head.next
        return middle            