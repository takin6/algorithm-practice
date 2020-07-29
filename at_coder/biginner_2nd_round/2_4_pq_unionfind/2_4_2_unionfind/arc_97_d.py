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
A = list(map(int,input().split()))
uf = UF(N+1)
for _ in range(M):
  u,v = map(int,input().split())
  uf.union(u,v)

res = 0
for i in range(N):
  if i+1 == A[i] or uf.same(i+1, A[i]):
    res += 1

print(res)
