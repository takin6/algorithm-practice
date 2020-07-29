# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        stack = [root]

        for i in preorder[1:]:
            new_node = TreeNode(i)
            if i < stack[-1].val:
                stack[-1].left = new_node
            else:
                while stack and stack[-1].val < i:
                    last = stack.pop()
                last.right = new_node
            stack.append(new_node)
        
        return root

# [8,5,1,7,10,12]

print(Solution().bstFromPreorder([8,5,1,7,10,12]))