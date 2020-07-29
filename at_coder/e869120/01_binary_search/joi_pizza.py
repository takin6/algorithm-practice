# D = int(input())
# N = int(input())
# M = int(input())

# S = [0]
# for _ in range(N-1):
#   S.append(int(input()))
# S.append(D)

# T = []
# for _ in range(M):
#   T.append(int(input()))

# S.sort()
# res = 0
# for t in T:
#   ok,ng = -1,len(S)
#   while abs(ok-ng) > 1:
#     mid = (ok+ng) // 2
#     if S[mid] <= t:
#       ok = mid
#     else:
#       ng = mid
#   res += min(t-S[ok], S[ok+1]-t)

# print(res)

# import bisect
# def I(): return int(input())
# d = I()
# n = I()
# m = I()
# dn = [0]+sorted([I() for _ in range(n-1)])+[d]
# mn = sorted([I() for _ in range(m)])
# ans = 0
# for x in mn:
#     ok = bisect.bisect(dn,x)-1
#     ans += min(x-dn[ok],dn[ok+1]-x)
# print(ans)

while True:
  D = int(input())
  if D==0: exit()
  N = int(input())
  M = int(input())
  shops = [0]
  for _ in range(N-1):
    shops.append(int(input()))
  shops.append(D)
  shops.sort()

  res = 0
  for _ in range(M):
    x = int(input())
    ok,ng = -1,len(shops)
    while abs(ok-ng)>1:
      mid = (ok+ng)//2
      if shops[mid] <= x:
        ok = mid
      else:
        ng = mid
    res += min(x-shops[ok], shops[ok+1]-x)

  print(res)


