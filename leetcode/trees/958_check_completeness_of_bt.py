# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # self.result = True

        # def dfs(root):
        #     if not root: return 

        #     if root.right:
        #         if not root.left:
        #             self.result = False
        #             return False

        #     re = dfs(root.right)

        #     # import pdb; pdb.set_trace()
        #     if re is None and root.left:
        #         if not root.right:
        #             self.result = False
        #             return False

        #     dfs(root.left)

        # dfs(root)
        # return self.result

        q = [(root, 1)]

        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1

            if node:
              nodes.append(node.left, 2*v)
              nodes.append(node.right, 2*v+1)

        return nodes[-1][1] == len(nodes)

# [1,2,3,4,5,null,7]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left, t.left.right = TreeNode(4), TreeNode(5)
t.right.right = TreeNode(7)

print(Solution().isCompleteTree(t))


# [1,2,3,5,null,7,8]
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(5)
t.right.left = TreeNode(7)
t.right.right = TreeNode(8)

print(Solution().isCompleteTree(t))