
N, Q = list(map(int, input().split()))

class UnionFind():
  def __init__(self, n):
    # size
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      # return node x
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y: return

    # x, y = 3, 1
    # self.parents[x], self.parents[y] = -2, -1
    # in case that size of parents is smaller than x
    if self.parents[x] > self.parents[y]:
      # x, y = 1, 3
      x, y = y, x

    # self.parents[1] = -1 + self.parents[3] (-2)
    self.parents[x] += self.parents[y]
    # self.parents[3] = 1
    self.parents[y] = x

  def same(self, x, y):
    return self.find(x) == self.find(y)

uf = UnionFind(N)
for _ in range(Q):
  a, u, v = list(map(int, input().split()))

  if a == 0:
    uf.union(u, v)
  else:
    print("Yes" if uf.same(u, v) else "No")


# 8 9
# 0 1 2
# parents = [-1, -2, 1, -1, -1, -1, -1, -1]
# 0 3 2
# x, y = 1, 3
# parents.x, parents.y = -2,-1
# x, y = 3, 1
# parents.3 (-1) = -1 + parents.1 (-2)
# parents.1 = 3




# 1 1 3
# 1 1 4
# 0 2 4
# 1 4 1
# 0 4 2
# 0 0 0
# 1 0 0

# yes 
# no
# yes
# yes