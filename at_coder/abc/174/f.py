import sys
from operator import itemgetter
 
sys.setrecursionlimit(500005)
stdin = sys.stdin
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().strip()
 
n, q = na()
a = na()
lasts = [-1] * (n+1)
rs = []
for i in range(n):
  if lasts[a[i]] != -1:
    rs.append((lasts[a[i]], i))
  lasts[a[i]] = i
 
rs.sort(key=itemgetter(0))
 
qs = []
for i in range(q):
  u = na()
  qs.append((u[0]-1, u[1]-1, i))
qs.sort(key=itemgetter(0))
 
def addfenwick(ft, i, v):
  if v == 0 or i < 0: return
  i += 1
  while i < len(ft):
    ft[i] += v
    i += i&-i
 
def sumfenwick(ft, i):
  s = 0
  i += 1
  while i > 0:
    s += ft[i]
    i -= i&-i
  return s
 
ft = [0] * (n+10)
anss = [0] * q
p = len(rs)-1
for q in qs[::-1]:
  while p >= 0 and rs[p][0] >= q[0]:
    addfenwick(ft, rs[p][1], 1)
    p -= 1
  anss[q[2]] = q[1]-q[0]+1-sumfenwick(ft, q[1])
 
for v in anss:
  print(v)

# https://atcoder.jp/contests/abc174/submissions/15613555

