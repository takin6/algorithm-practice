class UF():
  def __init__(self, n):
    self.parents = [-1] * n

  def find(self,n):
    if self.parents[n] < 0:
      return n
    else:
      self.parents[n] = self.find(self.parents[n])
      return self.parents[n]

  def union(self, u, v):
    p1, p2 = self.find(u), self.find(v)
    if p1 == p2: return

    if self.parents[p1] > self.parents[p2]:
      p1,p2 = p2,p1

    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def same(self, u, v):
    return self.find(u) == self.find(v)

V,E = map(int,input().split())
edges = []
for i in range(E):
  s,t,w = map(int,input().split())
  edges.append((w,s,t))
edges.sort(key=lambda x: x[0])

uf = UF(V)
ans = 0
for i in range(E):
  w,s,t = edges[i]
  if not uf.same(s,t):
    uf.union(s,t)
    ans += w

print(ans)