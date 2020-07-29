# 13
# 0 3 1 4 10
# 1 2 2 3
# 2 0
# 3 0
# 4 3 5 6 7
# 5 0
# 6 0
# 7 2 8 9
# 8 0
# 9 0
# 10 2 11 12
# 11 0
# 12 0

class TreeNode():

  def __init__(self, val, parent=-1):
    self.val = val
    self.children = []
    self.parent_val = parent
    self.depth = None

  def node_type(self):
    if self.depth == 0:
      return "root"
    elif len(self.children) > 0:
      return "internal node"
    else:
      return "leaf"

  def children_values(self):
    return [ c.val for c in self.children ]

  def __str__(self):
    return "node {0}: parent = {1}, depth = {2}, {3}, {4}".format(str(self.val), str(self.parent_val), str(self.depth), self.node_type(), self.children_values())

def calc_depths(node, level):
  node.depth = level
  for ch in node.children:
    calc_depths(ch, level+1)

num = int(input())
nodes = {}

for i in range(num):
  ins = list(map(int, input().split()))
  val = ins[0]

  if nodes.get(ins[0]) is None:
    nodes[val] = TreeNode(val)

  n = nodes[val]
  if ins[1] > 0:
    for j in ins[2:]:
      nodes.setdefault(j, TreeNode(j, n.val))
      n.children.append(nodes[j])
      nodes[j].parent_val = n.val

parent = [node for node in nodes.values() if node.parent_val == -1][0]
calc_depths(parent, 0)
sort_nodes = sorted(nodes.items(), key=lambda x:x[0] )

for _, node in sort_nodes:
  print(node)

