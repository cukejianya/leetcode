# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """""
        array = []
        stack = [root]
        seen = set()
        while (stack):
            curr = stack.pop()
            if curr == None:
                array.append(curr)
                continue
            seen.add(curr)
            array.append(curr.val)
            if not curr.left in seen:
                stack.append(curr.left)
            if not curr.right in seen:
                stack.append(curr.right)
        return str(array)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """""
        # Your Codec object will be instantiated
        # and called as such:
        # Your Codec object will be instantiated
        # and called as such:
        # ser = Codec()
        # deser = Codec()
        # tree = ser.serialize(root)
        # ans = deser.deserialize(tree)
        # return ans
        """"
        """"
        array = list(str)
        root_val = array.pop(0)
        return self.dfs(Node(root_val), array) if root_val else root_val
    
    def dfs(self, root, array):
        left = array.pop(0)
        right = array.pop(0)
        root.left = Node(left) if left else left
        root.right = Node(right) if right else right
        dfs(root.left, array)
        dfs(root.right, array)
