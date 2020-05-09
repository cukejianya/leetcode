# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [[root]]
        found = False
        while queue:
            curr_level = queue.pop(0)
            new_level = []
            for node_idx in range(len(curr_level)):
                node = curr_level[node_idx]
                if not node:
                    continue
                isSibling = (found % 2 == 0 and node_idx == found + 1) 
                if found and node.val in [x, y] and not isSibling:
                    return True
                if node.val in [x, y]:
                    found = node_idx
                if node.left or node.right:
                    new_level.append(node.left)
                    new_level.append(node.right)
            if found:
                return False
            queue.append(new_level)
        return False