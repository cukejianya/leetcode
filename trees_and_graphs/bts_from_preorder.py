class Solution:
    def bstFromPreorder(self, preorder):
        root = Treenode(preorder.pop(0))
        root.left = self.bstFromPreorder(preorder)
        root.right = self.bstFromPreorder(preorder)
        return root