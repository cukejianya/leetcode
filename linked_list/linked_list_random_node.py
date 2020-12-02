# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head
        self.node_total_count = 1
        curr = head
        while curr.next :
            self.node_total_count += 1
            curr = curr.next

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        curr = self.head
        random_pos = random.randint(1, self.node_total_count)
        for x in range(random_pos - 1):
            curr = curr.next
        return curr.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
