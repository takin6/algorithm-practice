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

H,W = map(int,input().split())
sx,sy = list(map(int, input().split()))
S = (sx-1,sy-1)
gx,gy = list(map(int, input().split()))
G = (gx-1,gy-1)

p = []
total = 0
for i in range(H):
  p.append(list(map(int, input().split())))
  total += sum(p[i])

edges = []
# nid = 0
for i in range(H):
  for j in range(W):
    # if i-1 >= 0:
    #   heapq.heappush(edges, (-p[i][j]*p[i-1][j], nid, nid-H))
    if i+1 < H:
      # heapq.heappush(edges, (-p[i][j]*p[i+1][j], nid, nid+H))
      heapq.heappush(edges, (-p[i][j]*p[i+1][j], i*W+j, (i+1)*W+j))
    # if j-1 >= 0:
    #   heapq.heappush(edges, (-p[i][j]*p[i][j-1], nid, nid-1))
    if j+1 < W:
      heapq.heappush(edges, (-p[i][j]*p[i][j+1], i*W+j, i*W+j+1))
    # nid += 1

uf = UF(H*W)
while edges:
  c,u,v = heapq.heappop(edges)
  if not uf.same(u,v):
    total += -c
    uf.union(u,v)

print(total)