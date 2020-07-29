N, Q = map(int, input().split())

class UF():
  def __init__(self):
    self.parents = [-1] * (N+1)

  def union(self, f, t):
    x = self.find(f)
    y = self.find(t)
    if x == y:
      return

    if self.parents[x] > self.parents[y]:
      x,y = y,x
    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def same(self, n1, n2):
    return self.find(n1) == self.find(n2)

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

uf = UF()
for _ in range(Q):
  q, n1, n2 = map(int, input().split())
  if q == 0:
    uf.union(n1,n2)
  if q == 1:
    print("Yes") if uf.same(n1,n2) else print("No")