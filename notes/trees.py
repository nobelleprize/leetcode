# Trees
# BFS/level order

def levelOrder(root):
    if root == None:
        return

    queue = []
    queue.append(root)

    while queue:
        print(queue[0].data)
        
        node = queue.pop(0)

        if node.left != None:
            queue.append(node.left)

        if node.right != None:
            queue.append(node.right)