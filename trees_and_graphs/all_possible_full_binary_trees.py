# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N: int):
        N -= 1
        return self.getSubFBT(N)
    
    def getSubFBT(self, N: int):
        if N == 0:
            return [TreeNode(0)]
        N -= 2
        subFBT = []
        left_array = []
        right_array = []
        print(N ,list(range(0, int(N/2) + 2, 2)))
        for i in range(0, int((N+2)/2), 2):
            print(N, i)
            left_array = self.getSubFBT(i)
            right_array = self.getSubFBT(N - i)
            print(N, left_array, i, right_array, N - i)
            subFBT += self.createParentNodes(left_array, right_array)
            print( self.createParentNodes(left_array, right_array))
        return subFBT

    def createParentNodes(self, left_array, right_array):
        parent_node_list = []
        for left_child_node in left_array:
            for right_child_node in right_array:
                parent_node = TreeNode(0)
                parent_node.left = left_child_node
                parent_node.right = right_child_node
                opposite_parent_node = TreeNode(0)
                opposite_parent_node.left = right_child_node
                opposite_parent_node.right = left_child_node
                parent_node_list.append(parent_node)
                parent_node_list.append(opposite_parent_node)
        return parent_node_list
