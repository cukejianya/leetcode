class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        queue = [[root]]
        total = 0
        while(queue):
            curr_level = queue.pop(0)
            next_level = []
            for node in curr_level:
                total += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if next_level:
                queue.append(next_level)
                total = 0
        return total