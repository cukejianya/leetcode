class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        total = 0
        queue = [root]
        even_children = set()
        while(queue):
            curr = queue.pop(0)
            if curr in even_children:
                total += curr.left.val if curr.left else 0
                total += curr.right.val if curr.right else 0
            if curr.val % 2 == 0:
                (curr.left and even_children.add(curr.left)) 
                (curr.right and even_children.add(curr.right)) 
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return total