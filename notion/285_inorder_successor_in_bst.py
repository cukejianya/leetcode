# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':
        stack = [root]
        seen = set()
        while(stack):
            curr_node = stack[-1]
            if curr_node.left and not curr_node.left in seen:
                stack.append(curr_node.left)
            else:
                seen.add(stack.pop())
                if curr_node.val > p.val:
                    return curr_node
                if curr_node.right and not curr_node.right in seen:
                    stack.append(curr_node.right)
        return None
