# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from quopri import decodestring


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

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.serializeUtil(root,"")
    
    def serializeUtil(self, root, string):
        if root is None:
            string += "None,"
        else:
            string += str(root.val) + ","
            string = self.serializeUtil(root.left, string)
            string = self.serializeUtil(root.right, string)
        
        return string
            
        

    def deserialize(self, data):
        data_list = data[1:].split(",")
        root = self.deserializeUtil(data_list)
        return root
    
    def deserializeUtil(self, arr):
        if arr[0] == "None":
            arr.pop(0)
            return None
        
        root = TreeNode(arr[0])
        arr.pop(0)
        root.left = self.deserializeUtil(arr)
        root.right = self.deserializeUtil(arr)
        
        return root

c = Codec()
root = c.deserialize("[1,2,None,None,5,None,None,]")
drawtree(root)

print(c.serialize(root))


            