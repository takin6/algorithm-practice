N,M = map(int,input().split())
keys = []
for _ in range(M):
  a,b = map(int,input().split())

  s = 0
  for c in list(map(int,input().split())):
    c -= 1
    s = s | 1<<c

  keys.append((s, a))


# dp[i][j] = Nの状態の鍵を用いた時に、Mの鍵を開けるための最小コスト
dp = [float('inf')] * (1<<N)
dp[0] = 0
for s in range(1<<N):
  for i in range(M):
    t = s | keys[i][0]
    cost = dp[s] + keys[i][1]
    dp[t] = min(dp[t], cost)

if dp[-1] == float('inf'):
  print(-1)
else:
  print(dp[-1])