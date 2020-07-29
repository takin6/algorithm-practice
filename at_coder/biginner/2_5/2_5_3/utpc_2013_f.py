class UF():
  def __init__(self, N):
    self.par = [-1]*N

  def find(self, x):
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def union(self, x,y):
    p1,p2 = self.find(x),self.find(y)
    if p1 == p2: return
    if p1 > p2:
      p1,p2 = p2,p1
    self.par[p1] += self.par[p2]
    self.par[p2] = p1

  def same(self, x,y):
    return self.find(x) == self.find(y)

N,M = map(int, input().split())
edges = []
for _ in range(M):
  s,d,c = map(int,input().split())
  edges.append([c,s-1,d-1])
edges.sort(key=lambda x: x[0])

original_costs = 0
mst_edges = []
uf = UF(N)
for c,s,d in edges:
  if not uf.same(s,d):
    original_costs += c
    uf.union(s,d)
    mst_edges.append([c,s,d])

