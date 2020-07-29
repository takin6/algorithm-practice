# class UF():
#   def __init__(self, N):
#     self.parents = [ i for i in range(N+1) ]

#   def union(self, f, t):
#     p1 = self.find(f)
#     p2 = self.find(t)
#     if p1 == p2:
#       return
#     self.parents[p2] = p1

#   def find(self, node):
#     # if self.parents[node] == node:
#     #   return node
#     # else:
#     #   return self.find(self.parents[node])
#     while self.parents[node] != node:
#       node = self.parents[node]
#     return node

class UF():
  def __init__(self, N):
    self.parents = [-1] * (N+1)

  def union(self, f, t):
    p1 = self.find(f)
    p2 = self.find(t)
    if p1 == p2:
      return

    if self.parents[p1] > self.parents[p2]:
      p1,p2 = p2,p1
    self.parents[p1] += self.parents[p2]
    self.parents[p2] = p1

  def find(self, node):
    if self.parents[node] < 0:
      return node
    else:
      self.parents[node] = self.find(self.parents[node])
      return self.parents[node]

  def same(self, n1, n2):
    return self.find(n1) == self.find(n2)

N,M = map(int, input().split())
p = list(map(int, input().split()))
uf = UF(N)
xy = [ list(map(int, input().split())) for _ in range(M) ]

# for _ in range(M):
#   x,y = map(int, input().split())
#   uf.union(x,y)
for x,y in xy:
  uf.union(x,y)

res = 0
for i in range(N):
  if i+1 == p[i] or uf.same(i+1, p[i]):
    res += 1

print(res)


# groups = {}
# for i in range(1, N+1):
#   if uf.parents[i] in groups:
#     groups[uf.parents[i]].append(i)
#   else:
#     groups[uf.parents[i]] = [i]