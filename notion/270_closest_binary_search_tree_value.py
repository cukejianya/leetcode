# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr_node = root
        seen = set()
        closet_node = root
        while(curr_node):
            if abs(target - curr_node.val) < abs(target - closet_node.val):
               closet_node = curr_node 
            if target == curr_node.val:
                return curr_node.val
            if target < curr_node.val:
                curr_node = curr_node.left 
            elif target > curr_node.val:
                curr_node = curr_node.right
        return closet_node.val