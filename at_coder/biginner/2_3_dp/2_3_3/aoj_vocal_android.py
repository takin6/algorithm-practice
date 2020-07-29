# N = int(input())
# # S,L,P = [], [], []
# # for i in range(N):
# #   s,l,p = map(int, input().split())
# #   S.append(s)
# #   L.append(l)
# #   P.append(p)
# P = [0]*394
# for i in range(N):
#   s,l,p = map(int, input().split())
#   for i in range(s, l+1):
#     if p > P[i]:
#       P[i] = p

# PHRASE = [ int(input()) for _ in range(int(input()))]
# M = max(PHRASE)

# # dp = [ [-1]*(M+1) for _ in range(N+1)]
# dp = [ [-1]*(M+1) for _ in range(395)]

# for i in range(395): dp[i][0] = 0

# for i in range(1, 395):
#   for m in range(M+1):
#     if i <= m:
#       # for k in range(S[i-1], L[i-1]+1):
#       #   if m-k >= 0 and dp[i-1][m-k] != -1:
#           # dp[i][m] = max(dp[i][m], dp[i-1][m-k]+P[i-1])
#       # dp[i][m] = max(dp[i][m], dp[i-1][m-i]+P[i-1], dp[i][m-i]+P[i-1])
#       if dp[i-1][m-i] > -1:
#         dp[i][m] = max(dp[i-1][m], dp[i-1][m-i]+P[i-1])
#     else:
#       dp[i][m] = dp[i-1][m]


# res = [ dp[-1][ph] for ph in PHRASE ]

# print(dp)
# if -1 in res:
#   print(-1)
# else:
#   for r in res: print(r)

# N = int(input())
# points = [-1]*395
N = int(input())
points = [-1] * 394

for _ in range(N):
  s, l, p = map(int, input().split())
  for i in range(s, l + 1):
    points[i] = max(p, points[i])

for i in range(394):
  for j in range(i):
    points[i] = max(points[i], points[j]+points[i-j])

res = []
for _ in range(int(input())):
  res.append(points[int(input())])

if -1 in res:
  print(-1)
else:
  for r in res: print(r)
