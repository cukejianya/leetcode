def inorder_traversal(root):
    stack = [root]
    solution = []
    current = root
    while(stack):
        if current.left:
            stack.append(current.left)
            current = current.left
        else:
            solution.append(current)
            if current.right:
                stack.append(current.right)
    return solution
