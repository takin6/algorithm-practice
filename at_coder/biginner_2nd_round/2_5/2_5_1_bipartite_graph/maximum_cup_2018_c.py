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

  def size(self, x):
    return -self.par[self.find(x)]

N = int(input())
uf = UF(N)
for i in range(N):
  m = int(input())-1
  uf.union(i,m)
  if i == m:
    print(-1)
    exit()

for i in range(N):
  if uf.size(i) % 2 == 1:
    print(-1)
    exit()
print(N//2)
