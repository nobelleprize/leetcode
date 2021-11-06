import LinkedList as LL

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def preorderTraversal(root):
    if root:
        print(root.data)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

def connect(root):
    if not root:
        return 
    s = [root]

    while len(s):
        popped = s.pop()
        
        if popped.right:
            s.append(popped.right)
            
        if popped.left:
            s.append(popped.left)
        
        if len(s):
            popped.right = s[-1]
        
        popped.left = None



def flatten(root):
    # A global variable which maitains the last node
    # that was added to the linked list
    global last
    if(root == None):
        return

    # Avoid first iteration where root is
    # the only node in the list
    if(root != last):
        last.right = root
        last.left = None
        last = root
    flatten(root.left)
    flatten(root.right)
    if(root.left == None and root.right == None):
        last = root

def solution(root):
    result = []
    current = []

    if root != None:
        current.append(root)
    
    while len(current) > 0:
        result.append(current)
        parents = current
        current = []
    
        for parent in parents:
            if parent.left != None:
                current.append(parent.left)
            if parent.right != None:
                current.append(parent.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

last = root

res = solution(root)
for l in res:
    print(l[0].data)



        