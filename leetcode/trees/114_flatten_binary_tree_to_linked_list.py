# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = TreeNode(None)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if root is None: return

        self.flatten(root.left)
        self.flatten(root.right)

        root.right = self.prev
        root.left = None
        self.prev = root

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(5)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right.right = TreeNode(6)

Solution().flatten(t)
