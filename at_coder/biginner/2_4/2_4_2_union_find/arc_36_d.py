# class UF():
#   def __init__(self, N):
#     self.parents = [-1] * (N+1)

#   def union(self, f, t):
#     p1 = self.find(f)
#     p2 = self.find(t)
#     if p1 == p2:
#       return

#     if self.parents[p1] > self.parents[p2]:
#       p1,p2 = p2,p1
#     self.parents[p1] += self.parents[p2]
#     self.parents[p2] = p1

#   def find(self, node):
#     if self.parents[node] < 0:
#       return node
#     else:
#       self.parents[node] = self.find(self.parents[node])
#       return self.parents[node]

#   def same(self, n1, n2):
#     return self.find(n1) == self.find(n2)

# N,Q = map(int, input().split())
# uf = UF(2*N)
# for i in range(Q):
#   w, x, y, z = map(int, input().split())

#   if w == 1:
#     if z%2 == 0:
#       uf.union(2*x, 2*y)
#       uf.union(2*x+1, 2*y+1)
#     else:
#       uf.union(2*x, 2*y+1)
#       uf.union(2*x+1, 2*y)
#   else:
    