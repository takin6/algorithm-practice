class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        history = []

        def subtree_sum(root):
            if root is None: return 0

            s = root.val + subtree_sum(root.left) + subtree_sum(root.right)
            history.append(s)

            return s

        total = subtree_sum(root)
        return max( [x*(total-x) for x in history]) % (10**9+7) 
  
        # return max((x*(total-x)) for x in sums) % (10**9+7) 

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right.left = TreeNode(6)

print(Solution().maxProduct(t))