# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import defaultdict
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        dic = defaultdict(set)

        def dfs(root, level, position):
            if root is None: return

            dic[level].add(position)
            dfs(root.left, level+1, position*2)
            dfs(root.right, level+1, position*2+1)

        dfs(root, 0, 1)

        ans = 1
        for vals in dic.values():
            if len(vals) > 1:
                ans = max(ans, (max(vals) - min(vals) + 1))

        return ans

t = TreeNode(1)
t.left = TreeNode(3)
t.right = TreeNode(2)
t.left.left = TreeNode(5)
t.left.right = TreeNode(3)
t.right.right = TreeNode(9)

print(Solution().widthOfBinaryTree(t))