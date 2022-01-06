# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            return TreeNode(val=val, left=root);

        curr_lvl_nodes = [root]
        while(depth > 2):
            prev_lvl_nodes = curr_lvl_nodes
            curr_lvl_nodes = []
            for node in prev_lvl_nodes:
                if node.left:
                    curr_lvl_nodes.append(node.left)
                if node.right:
                    curr_lvl_nodes.append(node.right)
            depth -= 1
        for node in curr_lvl_nodes:
            node.left = TreeNode(val, left=node.left)
            node.right = TreeNode(val, right=node.right)
        return root
