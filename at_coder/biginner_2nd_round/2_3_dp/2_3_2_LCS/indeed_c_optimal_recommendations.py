N,M = map(int, input().split())
dp = [ [ [0]*101 for _ in range(101) ] for _ in range(101) ]
for _ in range(N):
  a,b,c,d = map(int, input().split())
  dp[a][b][c] = max(dp[a][b][c], d)

# dp[a][b][c] = a,b,cを満たす求職者が得られる最も高い年収

for a in range(101):
  for b in range(101):
    for c in range(101):
      if a-1 >= 0:
        dp[a][b][c] = max(dp[a][b][c], dp[a-1][b][c])
      if b-1 >= 0:
        dp[a][b][c] = max(dp[a][b][c], dp[a][b-1][c])
      if c-1 >= 0:
        dp[a][b][c] = max(dp[a][b][c], dp[a][b][c-1])

for _ in range(M):
  a,b,c = map(int,input().split())
  print(dp[a][b][c])