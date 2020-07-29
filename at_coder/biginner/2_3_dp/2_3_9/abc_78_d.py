N,Z,W = map(int,input().split())
a = list(map(int,input().split()))
memo = {}

def dfs(i, turn):
  if (i, turn) in memo:
    return memo[i, turn]

  if turn == 0:
    if i == 0:
      res = abs(W-a[-1])
    else:
      res = abs(a[i-1] - a[-1])
    for j in range(i+1, N):
      res = max(res, dfs(j, 1))
  else:
    if i == 0:
      res = abs(Z - a[-1])
    else:
      res = abs(a[i-1] - a[-1])
    for j in range(i+1, N):
      res = min(res, dfs(j, 0))

  memo[i, turn] = res
  return res

print(dfs(0, 0))


# dp[pos][turn] = turnの番で相手がposまでカードを引いている場合の最終スコア
# dp = [ [0]*2 for _ in range(N+1) ]

# for i in range(N, -1, -1):
#   # 先攻
#   x = Z if i == N else a[N-1]
#   y = a[i-1] if i else W
#   dp[i][0] = max( dp[i][0], abs(y - x))
#   for j in range(i+1, N):
#     dp[i][0] = max(dp[i][0], dp[j][1])

#   # 後攻
#   x = a[i-1] if i else Z
#   y = W if i == N else a[N-1]
#   dp[i][1] = min( dp[i][1], abs(x - a[N-1]))
#   for j in range(i+1, N):
#     dp[i][1] = max(dp[i][1], dp[j][0])

# res = -10**100
# for i in dp:
#   res = max(res, i[0])

# print(res)