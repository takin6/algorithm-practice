class UF():
  def __init__(self, N):
    self.par = [-1] * N

  def union(self, x, y):
    p1,p2 = self.find(x), self.find(y)
    if p1 == p2: return

    if self.par[p1] > self.par[p2]:
      p1,p2 = p2,p1
    self.par[p1] += self.par[p2]
    self.par[p2] = p1

  def find(self, x):
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def size(self, x):
    return -self.par[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

N,M,K = map(int,input().split())
uf = UF(N)
adj = [ [] for _ in range(N)]
for _ in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  adj[u].append(v)
  adj[v].append(u)
  uf.union(u,v)

res = []
for n in range(N):
  res.append(uf.size(n) - 1 - len(adj[n]))

for _ in range(K):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  if uf.same(u,v):
    res[u] -= 1
    res[v] -= 1

print(" ".join(map(str, res)))
