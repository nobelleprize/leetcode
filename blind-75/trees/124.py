# https://leetcode.com/problems/binary-tree-maximum-path-sum/
from audioop import maxpp


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

def maxPathSum(root):
    global max_sum
    max_sum = float("-inf")
    helper(root)

    return max_sum

def helper(root):
    global max_sum

    if root is None:
        return 0
    
    left = max(helper(root.left), 0)
    right = max(helper(root.right), 0)

    current_sum = root.val + left + right
    max_sum = max(current_sum, max_sum)

    return root.val + max(left, right)


# root = deserialize("[-4,-10,-5,-1,null,null,-6,-2,-3,-7,-9]")
# print(maxPathSum(root))

# root2 = deserialize("[-4,4,-5,-2,-3,null,3,null,null,null,null,1,8,null,null,null,null,null,null,null,null,6,7,9,10]")
# print(maxPathSum(root2))

root3 = deserialize("[1,2,3]")
print(maxPathSum(root3))