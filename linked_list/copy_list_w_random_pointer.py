class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        current = head
        node_set = {}
        prev_node = None
        while(current):
            if current in node_set:
                current_copy = node_set[current]
            else:
                current_copy = RandomListNode(current.label)
                node_set[current] = current_copy
            
            if current.random in node_set:
                current_copy.random = node_set[current.random]
            else:
                if current.random:
                    current_copy.random = RandomListNode(current.random.label)
                    node_set[current.random] = current_copy.random
            if prev_node:
                prev_node.next = current_copy
            prev_node = current_copy
            current = current.next
        return node_set[head]
