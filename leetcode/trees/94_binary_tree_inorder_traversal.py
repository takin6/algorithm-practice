from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.result = []

        def dfs(root):
            if root is None: return

            dfs(root.left)
            self.result.append(root.val)
            dfs(root.right)

        dfs(root)
        return self.result  


t = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)

print(Solution().inorderTraversal(t))
