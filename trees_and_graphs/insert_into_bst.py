class Solution:
    def insertIntoBST(self, root, val):
        node = root
        new_node = TreeNode(val)
        while(node):
            if node.val < val:
                if not node.right:
                    node.right = new_node
                    node = node.right
                node = node.right
            else:
                if not node.left:
                    node.left = new_node
                    node = node.left
                node = node.left
        return root if root else new_node