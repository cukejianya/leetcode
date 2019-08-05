import itertools
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int):
        if N % 2 == 0:
            return []

        all_trees = collections.defaultdict(list)
        all_trees[1] = [TreeNode(0)]

        for n in range(3, N + 1, 2):
            for k in range(1, n, 2):
                for left_tree, right_tree in itertools.product(
                        all_trees[k],
                        all_trees[n - k - 1]
                ):
                    tree = TreeNode(0)
                    tree.left = left_tree
                    tree.right = right_tree
                    all_trees[n].append(tree)

        return all_trees[N]
