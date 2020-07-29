
A, B = input(), input()
N, M = len(A), len(B)
dp = [ [0] * (N+1) for _ in range(M+1) ]

for i in range(N+1):
  dp[0][i] = i

for j in range(M+1):
  dp[j][0] = j

for i in range(1, M+1):
  for j in range(1, N+1):
    if B[i-1] != A[j-1]:
      dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j-1]+1, dp[i-1][j]+1)
    else:
      dp[i][j] = dp[i-1][j-1]

print(dp[-1][-1])
