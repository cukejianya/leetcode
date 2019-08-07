class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def create(self, arr):
        head = ListNode(arr[0])
        curr = head
        for x in arr[1:]:
            curr.next = ListNode(x)
            curr = curr.next 
        return head
    
    def getList(self, head):
        if not head:
            return []
        return [head.val] + self.getList(head.next)
