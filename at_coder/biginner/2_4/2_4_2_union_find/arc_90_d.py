class UF():
  def __init__(self, N):
    self.parents = [-1] * (N+1)
    self.diff_weight = [0] * (N+1)

  def union(self, f, t, w):
    w += self.diff_weight[f]
    w -= self.diff_weight[t]

    p1 = self.find(f)
    p2 = self.find(t)
    if p1 == p2:
      return

    if self.parents[p1] > self.parents[p2]:
      p1,p2 = p2,p1
      w = -w
    self.parents[p1] += self.parents[p2]
    self.diff_weight[p2] = w
    self.parents[p2] = p1

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      y = self.find(self.parents[x])
      self.diff_weight[x] += self.diff_weight[self.parents[x]]
      self.parents[x] = y
      return y

  def weight(self, x, y):
    self.find(x); self.find(y)
    return abs(self.diff_weight[y] - self.diff_weight[x])

  def same(self, n1, n2):
    # import pdb; pdb.set_trace()
    return self.find(n1) == self.find(n2)

N,M = map(int, input().split())
uf = UF(N)
flg = True
for _ in range(M):
  l,r,d = map(int, input().split())
  if uf.same(l, r):
    if uf.weight(l,r) != d:
      flg = False
      break
  else:
    uf.union(l,r,d)

print('Yes') if flg else print('No')

# ################ NOTE ################# #
# 1.union operations
# have to consider 2 kinds of operations
# 1) 大きいグループに属している気を小さいグループにマージするとき
# 3 2
# 1 2 3
# 2 3 7
# => diff_weight = [0 0 3 10]
# 2) 小さいグループに属しているメンバーを大きいグループにマージするとき
# 3 2
# 1 3 2
# 2 3 7
# => diff_weight = [0 0 -5 2]
#

# http://b1u3.hateblo.jp/entry/2019/11/19/192551
# https://qiita.com/drken/items/cce6fc5c579051e64fab