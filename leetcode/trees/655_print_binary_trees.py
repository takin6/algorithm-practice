from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def printTree(self, root: TreeNode) -> List[List[str]]:
    #     height = 0
    #     q = [(root, 1)]
    #     while q:
    #         cur_node, cur_h = q.pop(0)

    #         if cur_node is None: continue

    #         height = max(height, cur_h)
    #         q.append((cur_node.left, cur_h+1))
    #         q.append((cur_node.right, cur_h+1))


    #     col_size = (2 ** height) -1
    #     graph = [ [""] * col_size for _ in range(height)]

    #     q = [(root, 0, ((col_size-1) // 2))]
    #     while q:
    #         cur_node, level, col_idx = q.pop(0)

    #         if cur_node is not None:
    #             graph[level][col_idx] = str(cur_node.val)

    #             left_idx = [ i for i in range(0, col_idx) ]
    #             if left_idx:
    #               next_left_idx = left_idx[ len(left_idx) // 2]

    #             right_idx = [ i for i in range(col_idx+1, col_size) ]
    #             if right_idx:
    #               next_right_idx = right_idx[ len(right_idx) // 2]

    #             print("left")
    #             print(cur_node.left, next_left_idx)
    #             print("right")
    #             print(cur_node.right, next_right_idx)
    #             q.append((cur_node.left, level+1, next_left_idx))
    #             q.append((cur_node.right, level+1, next_right_idx))

    #     return graph

    def printTree(self, root: TreeNode) -> List[List[str]]:

        def get_height(node):
            if not node:
                return 0
            else:
                return 1 + max(get_height(node.left), get_height(node.right))

        def update_output(node, row, left, right):
            if not node: return

            mid = (left + right) // 2
            self.output[row][mid] = str(node.val)
            update_output(node.left, row+1, left, mid-1)
            update_output(node.right, row+1, mid+1, right)

        height = get_height(root)
        width = 2 ** height - 1
        self.output = [[''] * width for _ in range(height)]
        update_output(root, 0, 0, width-1)
        return self.output


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.right = TreeNode(4)


print(Solution().printTree(t))


# ["",1, "",''], 
# ["",2, "",3, ''], 
# ["",4, "",'']

# [1,2,3,null,4]

# wrong
[["","","","1","","",""],
["","2","","","","3",""],
["","","","","4","",""]]

# correct
[["","","","1","","",""],
["","2","","","","3",""],
["","","4","","","",""]]