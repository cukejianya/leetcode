class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        return self.merge_sort(head)

    def merge_sort(self, head):
        if not head or not head.next:
            return head
        mid, mid_next = self.get_middle(head)

        left = self.merge_sort(head)
        right = self.merge_sort(mid_next)
        self.merge(left, right)
        return current_next

    def get_middle(self, head):
        current = head
        double_current = head.next
        while(double_current):
            double_current = double_current.next
            if double_current:
                double_current = double_current.next
                current = current.next
        current_next = current.next
        current.next = None
        return (current, current_next)
    
    def merge(self, left, right):
        pre_head = ListNode(None)
        current = pre_head
        while(right and left):
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next
        if not right:
            current.next = left
        else:
            current.next = right

        return pre_head.next 
