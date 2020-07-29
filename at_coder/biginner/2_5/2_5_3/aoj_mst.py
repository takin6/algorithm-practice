class UF():
  def __init__(self, N):
    self.par = [-1]*N

  def find(self, x):
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def union(self, x, y):
    p1,p2 = self.find(x),self.find(y)
    if p1 == p2: return

    if p1 > p2:
      p1,p2 = p2,p1
    self.par[p1] += self.par[p2]
    self.par[p2] = p1

  def same(self, x, y):
    return self.find(x) == self.find(y)


V,E = map(int, input().split())
edges = []
for _ in range(E):
  s,t,w = map(int, input().split())
  edges.append([s,t,w])
edges.sort(key=lambda x: x[2])

res = 0
uf = UF(V)
for u,v,w in edges:
  if not uf.same(u,v):
    res += w
    uf.union(u,v)

print(res)
