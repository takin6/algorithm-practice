# n, m = list(map(int, input().split()))
# C = sorted(list(map(int, input().split())))
# dp = [float('inf')] * (n+1)
# dp[0] = 0
# res = float('inf')

# for c in C:

#   for i in range(1,n+1):
#     if i >= c:
#       rem = i % c

#       if dp[rem] != float('inf'):
#         dp[i] = min(dp[i], i//c+dp[rem])

#   res = min(res, dp[-1])

n, m = list(map(int, input().split()))
C = sorted(list(map(int, input().split())))
dp = [float('inf')] * (n+1)
dp[0] = 0
res = float('inf')

for c in C:

  for i in range(1,n+1):
    if i >= c:
      dp[i] = min(dp[i], 1+dp[i-c])

  res = min(res, dp[-1])

print(res)