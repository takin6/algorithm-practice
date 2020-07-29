# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.ans = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node, depth, history):
            if node:
                if depth > 1:
                    if history[depth-2] % 2 == 0:
                        # print(node.val, history[depth-2], self.ans)
                        self.ans += node.val
                history[depth] = node.val

                dfs(node.left, depth+1, history)
                dfs(node.right, depth+1, history)

        history = [0] * (10**4)
        dfs(root, 0, history)

        return self.ans

# root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
        
t = TreeNode(6)
t.left = TreeNode(7)
t.right = TreeNode(8)

t.left.left = TreeNode(2)
t.left.right = TreeNode(7)

t.right.left = TreeNode(1)
t.right.right = TreeNode(3)

t.left.left.left = TreeNode(9)

t.left.right.left = TreeNode(1)
t.left.right.right = TreeNode(4)

t.right.right.right = TreeNode(5)

print(Solution().sumEvenGrandparent(t))