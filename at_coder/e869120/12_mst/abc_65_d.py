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

n = int(input())
coords = []
for i in range(n):
  x,y = map(int,input().split())
  coords.append((i,x,y))

edges = []

sorted_x = sorted(coords, key=lambda x: x[1])
for i in range(n-1):
  c = abs(sorted_x[i][1] - sorted_x[i+1][1])
  u,v = sorted_x[i][0], sorted_x[i+1][0]
  edges.append((c,u,v))

sorted_y = sorted(coords, key=lambda x: x[2])
for i in range(n-1):
  c = abs(sorted_y[i][2] - sorted_y[i+1][2])
  u,v = sorted_y[i][0], sorted_y[i+1][0]
  edges.append((c,u,v))

edges.sort()

uf = UF(n)
res = 0
for c,u,v in edges:
  if not uf.same(u,v):
    uf.union(u,v)
    res += c
 
print(res)


# edges = []
# for i in range(n):
#   for j in range(i+1, n):
#     x1,y1 = coords[i]
#     x2,y2 = coords[j]
#     c = min(abs(x1-x2), abs(y1-y2))
#     edges.append((c,i,j))
# edges.sort()

# print(edges)