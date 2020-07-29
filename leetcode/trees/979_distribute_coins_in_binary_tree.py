# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root):
            if root is None: return 0

            excess_from_left = dfs(root.left)
            excess_from_right = dfs(root.right)

            print(root.val, excess_from_left, excess_from_right)
            self.res += abs(excess_from_left) + abs(excess_from_right)
            return root.val + excess_from_left + excess_from_right - 1

        dfs(root)
        return self.res

# t = TreeNode(3)
# t.left = TreeNode(0)
# t.right = TreeNode(0)

# print(Solution().distributeCoins(t))

# print("---------------")
# t = TreeNode(0)
# t.left = TreeNode(3)
# t.right = TreeNode(0)
# print(Solution().distributeCoins(t))


print("---------------")
# [1,0,0,null,3]
t = TreeNode(1)
t.left = TreeNode(0)
t.right = TreeNode(0)
t.left.right = TreeNode(3)
print(Solution().distributeCoins(t))
