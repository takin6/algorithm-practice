# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        return self.cal([i for i in range(1, n+1)])
    
    def cal(self, lst):
        if not lst: return [None]
        res=[]
        for i in range(len(lst)):
            for left in self.cal(lst[:i]):
                for right in self.cal(lst[i+1:]):
                    node, node.left, node.right=TreeNode(lst[i]), left, right
                    res+=[node]
        return res

print(Solution().generateTrees(3))