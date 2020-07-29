class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(d)
            new_root.left = root

            return new_root


        q = [(root, 1, root)]
        to_change = []

        while q:
            node, level, parent = q.pop(0)

            if node is None: continue

            # if level - 1 == d:
            if level == d - 1:
                to_change.append(node)
            else:
                q.append((node.left, level+1, node))
                q.append((node.right, level+1, node))

        for parent in to_change:
            if parent.left:
                new = TreeNode(v)
                old = parent.left
                parent.left, new.left = new, old

            if parent.right:
                new = TreeNode(v)
                old = parent.right
                parent.right, new.right = new, old

        return root


t = TreeNode(4)
t.left = TreeNode(2)
t.right = TreeNode(6)
t.left.left = TreeNode(3)
t.left.right = TreeNode(1)
t.right.left = TreeNode(5)

Solution().addOneRow(t, 1, 2)