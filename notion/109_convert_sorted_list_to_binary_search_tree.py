# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        length = 0
        stack = []
        while curr_node:
            stack.append(curr_node)
            curr_node = curr_node.right
        curr_node = head
        idx = 0
        while idx == length // 2:
            curr_node = curr_node.right
            idx += 1
