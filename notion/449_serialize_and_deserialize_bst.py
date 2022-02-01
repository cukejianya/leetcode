# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode], tree_string="") -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return tree_string
        tree_string += str(root.val) + ','
        tree_string = self.serialize(root.left, tree_string) 
        tree_string = self.serialize(root.right, tree_string)
        return tree_string

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return []
        values = data.split(',')
        values.pop()
        values = [int(x) for x in values]
        root = TreeNode(values.pop(0))
        for x in values:
            curr_node = root
            while curr_node:
                prev_node = curr_node
                if x < curr_node.val: 
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            if x < prev_node.val:
                prev_node.left = TreeNode(x)
            else:
                prev_node.right = TreeNode(x)
        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
