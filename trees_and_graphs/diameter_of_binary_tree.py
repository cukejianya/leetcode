class Solution:
    def __init__(self, x):
        self.max_diameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        return find_diameter(root, [0])

    def find_diameter(self, root, height):
        if not root:
            height[0] = 0
            return 0
        left_height = [0]
        right_height = [0]
        left_diameter = find_diameter(root.left, left_height) 
        right_diameter = find_diameter(root.right, right_height) 
        height[0] = 1 + max(left_height, right_height)

        return max(1 + left_height + right_height, max(left_diameter,
                                                       right_diameter))