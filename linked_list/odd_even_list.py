class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd_node = even_node = even_head = None
        curr = head
        count = 1
        while (curr != None):
            if count % 2 == 1:
                if count == 1:
                    odd_node = curr
                else:
                    odd_node.next = curr
                    odd_node = curr
            else:
                if count == 2:
                    even_node = even_head = curr 
                else:
                    even_node.next = curr
                    even_node = curr
            count += 1
            curr = curr.next
        odd_node.next = even_head
        if even_node:
            even_node.next = None

        return head