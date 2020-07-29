class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def prune(root):
            if root is None: return False

            le, re = prune(root.left), prune(root.right)
            import pdb; pdb.set_trace()
            if not le: root.left = None
            if not re: root.right = None

            if root.val == 1 or le or re:
                return True
            else:
                return False
        
        prune(root)
        return root


t = TreeNode(1)
t.right = TreeNode(0)
t.right.left = TreeNode(0)
t.right.right = TreeNode(1)

print(Solution().pruneTree(t))