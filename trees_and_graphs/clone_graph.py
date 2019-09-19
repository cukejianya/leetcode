"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node
        for neighbor in node.neighbors:
            if neighbor in self.visited:
                clone_node.neighbors.append(self.visited[neighbor])
            else:
                clone_node.neighbors.append(self.cloneGraph(neighbor))
        return clone_node