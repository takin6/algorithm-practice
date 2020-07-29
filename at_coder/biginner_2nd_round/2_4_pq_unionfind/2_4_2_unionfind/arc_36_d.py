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


N,Q = map(int,input().split())
uf = UF(2*(N+1))
for _ in range(Q):
  w,x,y,z = map(int,input().split())
  if w == 1:
    if z%2 == 0:
      uf.union(x,y)
      uf.union(x+N,y+N)
    else:
      uf.union(x,y+N)
      uf.union(x+N,y)
  else:
    print("YES") if uf.same(x,y) else print("NO")

