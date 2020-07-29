class UF():
  def __init__(self, N):
    self.par = [-1] * N

  def find(self, n):
    if self.par[n] < 0:
      return n
    else:
      self.par[n] = self.find(self.par[n])
      return self.par[n]

  def union(self, x,y):
    p1,p2 = self.find(x), self.find(y)
    if p1 == p2: return
    if p1 > p2:
      p1,p2 = p2,p1
    self.par[p1] += self.par[p2]
    self.par[p2] = p1

  def same(self, x,y):
    return self.find(x) == self.find(y)

N,M = map(int,input().split())
uf = UF(N)
for _ in range(M):
  t,u,v = map(int,input().split())
  if t == 0:
    uf.union(u,v)
  else:
    print("Yes") if uf.same(u,v) else print("No")

