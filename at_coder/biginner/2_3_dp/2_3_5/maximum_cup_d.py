N,M,L,X = map(int,input().split())
A = list(map(int, input().split()))

dp = [ [X+1]*M for _ in range(N+1) ]
dp[0][0] = 1

for i in range(N):
  for j in range(M):
    if dp[i][j] == X+1: continue

    dp[i+1][j] = min(dp[i+1][j], dp[i][j])
    dp[i+1][(j+A[i])%M] = min(
      dp[i+1][(j+A[i])%M],
      dp[i][j]+(j+A[i])//M
    )

print("Yes" if dp[N][L] <= X else "No")

