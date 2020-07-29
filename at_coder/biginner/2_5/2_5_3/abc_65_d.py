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

N = int(input())
coordinates = []
for i in range(N):
  x,y = list(map(int, input().split()))
  coordinates.append((i,x,y))

edges = []

sort_x = sorted(coordinates, key=lambda x: x[1])
for i in range(N-1):
  u,v = sort_x[i][0], sort_x[i+1][0]
  edges.append([u,v,abs(sort_x[i][1] - sort_x[i+1][1])])

sort_y = sorted(coordinates, key=lambda x: x[2])
for i in range(N-1):  
  u,v = sort_y[i][0], sort_y[i+1][0]
  edges.append([u,v,abs(sort_y[i][2] - sort_y[i+1][2] )])

edges.sort(key=lambda x: x[2])
uf = UF(N)
res = 0
for u,v,c in edges:
  if not uf.same(u,v):
    uf.union(u,v)
    res += c

print(res)
