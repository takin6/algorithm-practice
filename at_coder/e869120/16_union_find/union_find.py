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

n,q = map(int,input().split())
uf = UF(n)
for _ in range(q):
  i,u,v = map(int,input().split())
  if i==0:
    uf.union(u,v)
  else:
    if uf.same(u,v):
      print(1)
    else:
      print(0)