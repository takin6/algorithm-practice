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

N,K,L = map(int,input().split())
uf_road = UF(N)
uf_railway = UF(N)

for _ in range(K):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  uf_road.union(u,v)

for _ in range(L):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  uf_railway.union(u,v)

dic = {}
counter = []
for i in range(N):
  p1 = uf_road.find(i)
  p2 = uf_railway.find(i)
  counter.append((p1,p2))
  if (p1,p2) not in dic:
    dic[(p1,p2)] = 1
  else:
    dic[(p1,p2)] += 1

for i in range(N):
  print(dic[counter[i]], end=" ")

# res = [1] * (N)
# for i in range(N):
#   for j in range(i+1, N):
#     if uf_road.same(i,j) and uf_railway.same(i,j):
#       res[i] += 1
#       res[j] += 1


