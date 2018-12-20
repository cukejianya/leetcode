class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first_node = head
        prev_node = None
        while(first_node):
            second_node = first_node.next
            if not second_node:
                return head
            first_node.next = second_node.next
            second_node.next = first_node
            if prev_node:
                prev_node.next = second_node
            else:
                head = second_node
            prev_node = first_node
            first_node = prev_node.next
        return head


