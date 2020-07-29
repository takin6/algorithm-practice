# import math  
# from collections import defaultdict
# N = int(input())
# MOD = 1000000007

# group = defaultdict(int)
# worst_iwashi_count = 0
# for _ in range(N):
#   a,b = map(int,input().split())

#   if a == 0 and b == 0:
#     worst_iwashi_count += 1
#     continue

#   if a == 0:
#     group[(0,-1)] += 1

#   if b == 0:
#     group[(1,0)] += 1

#   g = math.gcd(a,b)
#   a //= g
#   b //= g

#   if a < 0:
#     a *= -1
#     b *= -1

#   group[(a,b)] += 1

# ans = 1
# # import pdb; pdb.set_trace()
# items = [ (k,v) for k,v in group.items() ]
# for p,count in [ (k,v) for k,v in group.items() ]:
#   a,b = p
#   if b < 0:
#     pair_count = group[(-b, a)]
#     del group[(-b,a)]
#   else:
#     pair_count = group[(b,-a)]
#     del group[(b,-a)]

#   ans *= (2**count-1) + (2**pair_count-1) + 1
#   ans %= MOD

# print(ans + worst_iwashi_count - 1) % MOD


# https://ysk-pro.hatenablog.com/entry/abc168-e-bullet/


import math
N = int(input())
dic = {}
zz,az,bz = 0,0,0

for i in range(N):
  A,B = map(int,input().split())
  if A==B==0:
    zz += 1
  elif A==0:
    az += 1
  elif B==0:
    bz += 1
  else:
    g = math.gcd(A,B)
    A //= g
    B //= g
    if A*B > 0:
      now = (A,B)
      ind = 0
    else:
      # <0のパターンは、
      # (A,B) = (pos, neg)
      # (A,B) = (neg, pos)
      # => 前者の場合は、negを-1にすれば二つとも正になるが、後者の場合は、両方-1をかけなおす必要がある。
      now = (-1*B,A)
      ind = 1

    if now[0] < 0:
      now = (-1*now[0], -1*now[1])

    if now not in dic:
      dic[now] = [0,0]
    dic[now][ind] += 1

mod = 10**9+7
ans = pow(2, az, mod) + pow(2, az, mod) - 1
for i in dic:
  aa,bb = dic[i]
  now = pow(2, aa, mod) + pow(2, bb, mod) - 1
  ans *= now
  ans %= mod

print((ans - 1 + zz) % mod)

# https://atcoder.jp/contests/abc168/submissions/13323027