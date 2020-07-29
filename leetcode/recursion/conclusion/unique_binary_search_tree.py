from typing import List
from itertools import product

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def generateTrees(self, n: int) -> List[TreeNode]:
    #     return self.genTreeList(1, n)

    # def genTreeList(self, start, end):
    #     res = []

    #     if start > end:
    #         res.append(None)

    #     # i = 1, 2, 3
    #     for i in range(start, end+1):
    #         # start = 1
    #         # end = 0
    #         leftList = self.genTreeList(start, i-1)
    #         # start = 2
    #         # end = 3
    #         rightList = self.genTreeList(i+1, end)

    #         print(i)
    #         print(leftList, rightList)
    #         for leftNode in leftList:
    #             for rightNode in rightList:
    #                 root = TreeNode(i)
    #                 root.left = leftNode
    #                 root.right = rightNode
    #                 res.append(root)

    #     return res

    def generateTrees(self, n):
        return self.BST([i+1 for i in range(n)])
        
    def BST(self, nodes):
        trees = []
        for i in range(len(nodes)):
            # product : Cartesian product
            for leftSubTree, rightSubTree in product(self.BST(nodes[:i]), self.BST(nodes[i+1:])):
                if i == 1: import pdb; pdb.set_trace()
                root = TreeNode(nodes[i])
                root.left, root.right = leftSubTree, rightSubTree
                trees.append(root)
            
        return trees or [None]

print(Solution().generateTrees(3))