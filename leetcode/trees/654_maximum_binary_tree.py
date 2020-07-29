from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        RIGHT, LEFT = 1, 2

        def struct_tree(root, arr, d):
            if len(arr) == 0: return

            tmp_max = max(arr)
            new_root = TreeNode(tmp_max)
            if d == RIGHT:
              root.right = new_root
            if d == LEFT:
              root.left = new_root

            idx = arr.index(tmp_max)
            struct_tree(new_root, arr[:idx], LEFT)
            struct_tree(new_root, arr[idx+1:], RIGHT)

        m = max(nums)
        idx = nums.index(m)

        root = TreeNode(m)
        struct_tree(root, nums[:idx], LEFT)
        struct_tree(root, nums[idx+1:], RIGHT)

        return root

print(Solution().constructMaximumBinaryTree([3,2,1,6,0,5]))
r = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
import pdb; pdb.set_trace()
