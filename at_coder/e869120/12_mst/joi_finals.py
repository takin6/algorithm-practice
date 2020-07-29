class UF():
  def __init__(self, N):
    self.parents = [-1] * (N+1)

  def find(self, n):
    if self.parents[n] < 0:
      return n
    else:
      self.parents[n] = self.find(self.parents[n])
      return self.parents[n]

  def union(self, u,v):
    p1,p2 = self.find(u),self.find(v)
    if p1 == p2: return

    if p1 > p2:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def same(self, u, v):
    return self.find(u) == self.find(v)

N,M,K = map(int,input().split())
edges = []
for _ in range(M):
  u,v,c = map(int,input().split())
  edges.append((c,u,v))
edges.sort(key=lambda x: x[0])

if N==K:
  print(0)
  exit()

uf = UF(N)
ans = 0
f = N
for c,u,v in edges:
  if not uf.same(u,v):
    uf.union(u,v)
    ans += c
    f -= 1
  if f <= K:
    break

print(ans)
