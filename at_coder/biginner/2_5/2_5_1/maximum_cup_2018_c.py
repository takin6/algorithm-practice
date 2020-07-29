class UF():
  def __init__(self, N):
    self.par = [-1]*(N+1)

  def find(self, n):
    if self.par[n] < 0:
      return n
    else:
      self.par[n] = self.find(self.par[n])
      return self.par[n]

  def union(self, n1, n2):
    p1,p2 = self.find(n1),self.find(n2)
    if p1 == p2:
      return

    if p1 > p2:
      p1,p2 = p2,p1
    self.par[p1] += self.par[p2]
    self.par[p2] = p1

  def size(self, x):
    return self.par[self.find(x)]

  def same(self, n1, n2):
    return self.find(n1) == self.find(n2)

N = int(input())
uf = UF(N)
result = None
for i in range(1, N+1):
  t = int(input())
  if i == t:
    result = -1
  uf.union(i, t)

if result == -1:
  print(result)
  exit()

for i in range(1, N+1):
  if uf.size(i) % 2 == 1:
    print(-1)
    break
else:
  print(N//2)