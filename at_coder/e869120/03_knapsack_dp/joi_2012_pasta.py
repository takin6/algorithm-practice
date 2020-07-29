# dp[i][a][b] = i-2日目にaのパスタ、i-1日目にbのパスタを食べたときの
#               i日目のパスタの選び方

N,K = map(int,input().split())
menu = [0]*(N+1)
for _ in range(K):
  d,m = map(int,input().split())
  menu[d] = m

dp = [[0,0,0,0] for _ in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
  s = sum(dp[i-1])
  if menu[i] > 0:
    dp[i][menu[i]] = s
  else:
    for j in range(1,4):
      dp[i][j] = s

  if i>2:
    for j in range(1, 4):
      if dp[i][j] != 0 and dp[i-1][j] != 0:
        dp[i-1][j] -= dp[i-1][j]
        dp[i][j] -= dp[i-2][j]

print(menu)
print(list(range(1,N+1)))
for i in range(N+1):
  print(dp[i])
print(sum(dp[N]) % 10000)
