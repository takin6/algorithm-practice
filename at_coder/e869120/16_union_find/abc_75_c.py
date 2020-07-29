class UF():
  def __init__(self, N):
    self.parents = [-1] * N

  def find(self, n):
    if self.parents[n] < 0:
      return n
    else:
      self.parents[n] = self.find(self.parents[n])
      return self.parents[n]

  def union(self, u,v):
    p1,p2 = self.find(u),self.find(v)
    if p1==p2: return
    if p1 > p2:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def same(self, u,v):
    return self.find(u) == self.find(v)

N,M = map(int,input().split())
uf = UF(N+1)
ans = 0
edges = []
for _ in range(M):
  u,v = map(int,input().split())
  edges.append((u,v))

res = 0
for i in range(M):
  uf = UF(N+1)
  for j,edge in enumerate(edges):
    if i==j: continue
    uf.union(edge[0],edge[1])

  u,v = edges[i]
  if not uf.same(u,v):
    res += 1

print(res)
