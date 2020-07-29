class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    #     if root.val == val: return True, root
    #     if root.left is None or root.right is None: return False, None

    #     if not root.left is None or root.right is None:
    #         flag, ans = self.searchBST(root.left, val) or self.searchBST(root.right, val)

    #     return ans

    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None: return None

        if root.val == val:
            return root
        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)

        # if root and val < root.val: return self.searchBST(root.left, val)
        # elif root and val > root.val: return self.searchBST(root.right, val)
        # return root


        # if root and root.val == val:
        #     return root
        # if root and root.val > val:
        #     return self.searchBST(root.left, val)
        # elif root and root.val < val:
        #     return self.searchBST(root.right, val)

        # import pdb; pdb.set_trace()
        # return None

t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(7)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)

print(Solution().searchBST(t, 2))
print(Solution().searchBST(t, 5))

t = TreeNode(40)
t.left = TreeNode(20)
t.right = TreeNode(60)
t.left.left = TreeNode(10)
t.left.right = TreeNode(30)
t.right.left = TreeNode(50)
t.right.right = TreeNode(70)
print(Solution().searchBST(t, 25))
print(Solution().searchBST(t, 70))