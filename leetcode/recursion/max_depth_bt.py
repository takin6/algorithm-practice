class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(root, depth):
            if root is None: return depth
            return max(helper(root.left, depth+1), helper(root.right, depth+1))

        return helper(root, 0)


t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(Solution().maxDepth(t))
# [3,9,20,null,null,15,7]