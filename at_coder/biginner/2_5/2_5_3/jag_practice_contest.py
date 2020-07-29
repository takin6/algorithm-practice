import heapq

class UF():
  def __init__(self, N):
    self.par = [-1]*N

  def find(self, x):
    if self.par[x] < 0:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]

  def union(self, x,y):
    p1,p2 = self.find(x),self.find(y)
    if p1 == p2: return
    if p1 > p2:
      p1,p2 = p2,p1
    self.par[p1] += self.par[p2]
    self.par[p2] = p1

  def same(self, x,y):
    return self.find(x) == self.find(y)

while True:
  N,M = map(int, input().split())
  if N == 0 and M == 0: break
  edges = []
  for _ in range(M):
    u,v,c = map(int, input().split())
    edges.append((c,u-1,v-1))
  edges.sort(key=lambda x: x[0])

  uf = UF(N)
  cnt = N//2+1 if N%2==1 else N//2
  res = []
  for c,u,v in edges:
    if not uf.same(u,v):
      res.append(c)
      uf.union(u,v)
      cnt -= 1

    if cnt == 0:
      print(res[-1])
      break
