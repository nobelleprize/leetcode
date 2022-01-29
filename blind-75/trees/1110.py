class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1
    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()
    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0); turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

def delNodes(root, to_delete):
    result = []
    to_delete = set(to_delete)
    
    if root.val not in to_delete:
        result.append(root)

    helper(root, to_delete, result)

    return result

def helper(root, to_delete, result):
    if root is None:
        return None
    
    root.left = helper(root.left, to_delete, result)
    root.right = helper(root.right, to_delete, result)

    if root.val in to_delete:
        if root.left != None:
            result.append(root.left)
        if root.right != None:
            result.append(root.right)
        else:
            return None
    
    return root



root = deserialize("[1,2,3,4,5,6,7]")
res = delNodes(root, [1])
print(res)
drawtree(res[1])
        