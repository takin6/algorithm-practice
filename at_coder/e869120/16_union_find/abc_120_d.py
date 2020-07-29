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

  def weight(self, u):
    p = self.find(u)
    return -self.parents[p]

n,m = map(int,input().split())
edges = []
for _ in range(m):
  u,v = map(int,input().split())
  edges.append((u,v))
edges.reverse()

uf = UF(n+1)

ans = [n*(n-1)//2]
for i in range(m-1):
  if ans[-1] == 0:
    ans.append(0)
  else:
    u,v = edges[i]
    if uf.same(u,v):
      ans.append(ans[-1])
    else:
      w1,w2 = uf.weight(u), uf.weight(v)
      ans.append(ans[-1]-w1*w2)
      uf.union(u,v)

for a in ans[::-1]:
  print(a)