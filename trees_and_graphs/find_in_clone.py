class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original == target:
            return cloned
        if original is None:
            return None

        return getTargetCopy(original.left, cloned.left, target) or getTargetCopy(original.right, cloned.right, target)