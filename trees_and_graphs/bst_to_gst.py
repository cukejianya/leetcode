class Solution:
    def bstToGst(self, root):
        self.bstMod(root, 0)
        return root
    
    def bstMod(self, root, value):
        right_value = self.bstMod(root.right, value) if root.right else value
        root.val += right_value
        left_value = self.bstMod(root.left, root.val) if root.left else root.val
        return left_value 