# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode], paths=[]) -> List[str]:
        if not root:
            return []
        self.paths = []
        self.bfs(root, [])
        return self.paths

    def bfs(self, node, path):
        path.append(str(node.val))
        if not node.left and not node.right:
            self.paths.append("->".join(path))
        if node.left:
            self.bfs(node.left, path[::])
        if node.right:
            self.bfs(node.right, path[::])
    
