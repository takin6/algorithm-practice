# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        # ----- solution in DFS (preorder traversal) ---------
        cnt = {}

        def dfs(node, depth):
            if node:
                if cnt.get(depth) is None:
                    cnt[depth] = node.val
                else:
                    cnt[depth] += node.val

                dfs(node.left, depth+1)
                dfs(node.right, depth+1)

        dfs(root, 0)

        return cnt[max(cnt.keys())]

        # ------ solution in iteration --------------
        # if not root:
        #     return 0
        # q = [root]
        # while True:
        #     q_new = [ x.left for x in q if x.left ] 
        #     q_new += [ x.right for x in q if x.right ] 
        #     if not q_new:
        #         break
        #     q = q_new
        # return sum([ node.val for node in q ])
        
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)

t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

t.right.right = TreeNode(5)
t.right.right = TreeNode(6)

t.left.left.left = TreeNode(7)

t.right.right.right = TreeNode(8)

print(Solution().deepestLeavesSum(t))


# recurrence relation
# f(node) = node.val + f(node.left)

# 