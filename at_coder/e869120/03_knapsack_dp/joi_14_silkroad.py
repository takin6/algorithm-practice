# dp[i][j] = i日間かけて都市jに移動するときに消耗する体力の最小値

N,M = map(int,input().split())
D = [0]
for _ in range(N):
  D.append(int(input()))

C = [0]
for _ in range(M):
  C.append(int(input()))

INF = float('inf')
dp = [ [INF]*(N+1) for _ in range(M+1) ]
dp[0][0] = 0

# i日目
for i in range(M):
  c = C[i+1]
  # 都市j
  for j in range(min(i+1,N)):
    d = D[j+1]

    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+c*d)

res = INF
for i in range(M+1):
  res = min(res, dp[i][-1])

print(res)
# print(dp)
for d in dp:
  print(d)