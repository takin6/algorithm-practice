from collections import defaultdict
from math import gcd

K = int(input())
res = 0
for a in range(1, K+1):
  for b in range(1, K+1):
    for c in range(1, K+1):
      res += gcd(gcd(a,b),c)

print(res)
# dp = defaultdict(int)

# def gcd(a,b):
#   a,b = sorted([a,b])

#   k = "".join([ str(x) for x in [a,b]])
#   # if not dp[k]:
#   #   # dp[k] = F(a,b)
#   dp[k] = math.gcd(a,b)

#   return dp[k]

# tmp = []
# for a in range(1, K+1):
#   for b in range(1, K+1):
#     k = "".join([ str(x) for x in sorted([a,b])])

#     if not dp[k]:
#       dp[k] = gcd(a,b)

#     tmp.append(dp[k])

# res = 0
# for t in tmp:
#   for c in range(1, K+1):
#     k = "".join([ str(x) for x in sorted([t,c])])

#     # if not dp[k]:
#     #   dp[k] = gcd(t,c)

#     res += gcd(t,c)

# print(res)
