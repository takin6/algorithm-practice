# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        # if not root: return 0

        # RIGHT, LEFT = 1, -1
        # result = 0
        # q = []

        # if root.left:
        #     q.append((root.left, LEFT, 1))
        # if root.right:
        #     q.append((root.right, RIGHT, 1))

        # while q:
        #     node, dct, max_size = q.pop(0)
        #     result = max(result, max_size)

        #     if node.left:
        #         if dct == LEFT: # came from left
        #             q.append((node.left, LEFT, 1))
        #         if dct == RIGHT:
        #             q.append((node.left, LEFT, max_size+1))

        #     if node.right:
        #         if dct == LEFT:
        #             q.append((node.right, RIGHT, max_size+1))
        #         if dct == RIGHT:
        #             q.append((node.right, RIGHT, 1))

        # return result
        result = 0

        def dfs(node, isLeft):
            if node is None: return 0

            l = dfs(node.left, False)
            r = dfs(node.right, True)

            result = max(result, l)
            result = max(result, r)

            if isLeft:
                return 1 + l
            else:
                return 1 + r

        dfs(root, True)