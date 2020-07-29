
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.deque = []

        q = [root]
        while q:
            node = q.pop(0)

            if node is None: continue

            if not node.left or not node.right:
                self.deque.append(node)

            if node.left:
                self.q.append(node.left)
            if node.right:
                self.q.append(node.right)

    def insert(self, v: int) -> int:
        node = self.deque[0]
        self.deque.append(TreeNode(v))

        if not node.left:
            node.left = self.deque[-1]
        else:
            node.right = self.deque[-1]
            self.deque.pop(0)

        return node.val

    def get_root(self) -> TreeNode:
        return self.root

t = TreeNode(1)
t.left, t.right = TreeNode(2), TreeNode(3)
t.left.left, t.left.right = TreeNode(4), TreeNode(5)
t.right.left = TreeNode(6)

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()