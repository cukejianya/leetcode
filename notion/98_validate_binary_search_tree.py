# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [root]
        seen = set()
        prev_val = float('-inf')
        curr_node = None
        while(stack):
            curr_node = stack[-1]
            if curr_node.left and not curr_node.left in seen:
                stack.append(curr_node.left)
            else:
                curr_node = stack.pop()
                if prev_val >= curr_node.val:
                        return False
                seen.add(curr_node)
                prev_val = curr_node.val
                if curr_node.right and not curr_node.right in seen:
                    stack.append(curr_node.right)
        return True