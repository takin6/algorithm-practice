# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindElements:

    # def __init__(self, root: TreeNode):
    #     self.root = root
    #     self.root.val = 0
    #     self.vals = []

    #     self.clean(root)
    
    # def clean(self, root):
    #     if root is None: return 0
        
    #     if root.left is not None:
    #         root.left.val = root.val * 2 + 1
    #         self.vals.append(root.val * 2 + 1)

    #     if root.right is not None:
    #         root.right.val = root.val * 2 + 2
    #         self.vals.append(root.val * 2 + 2)
        
    #     self.clean(root.left)
    #     self.clean(root.right)

    def __init__(self, root: TreeNode):
        self.root = root
        # self.root.val = 0
        self.vals = []

        self.clean(root, 0)
    
    def clean(self, root, val):
        if root:
            print(val)
            root.val = val
            self.vals.append(root.val)
            
            self.clean(root.left, root.val * 2+1)
            self.clean(root.right, root.val * 2+2)


    def find(self, target: int) -> bool:
        if target in self.vals:
            return True
        
        return False

t = TreeNode(-1)
t.right = TreeNode(-1)

f = FindElements(t)
import pdb; pdb.set_trace()