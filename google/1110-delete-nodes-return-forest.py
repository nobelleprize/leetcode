# https://leetcode.com/problems/delete-nodes-and-return-forest/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delNodes(root, to_delete):
    to_delete_set = set(to_delete)
    res = []
    helper(root, True, to_delete_set, res)
    return res
    

def helper(root, is_root, to_delete_set, result):
    if not root: 
        return None

    root_deleted = root.val in to_delete_set

    if is_root and not root_deleted:
        result.append(root)

    root.left = helper(root.left, root_deleted, to_delete_set, result)
    root.right = helper(root.right, root_deleted, to_delete_set, result)
    
    if root_deleted:
        return None
    else:
        return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = delNodes(root, [3,5])
for node in result:
    print(node.val)
