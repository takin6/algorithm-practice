N,M,S = map(int, input().split())

dp = [ [1]*(S+1)for _ in range(N*N+1) ]
mod = 100000

for i in range(2, N*N+1):
  for j in range(S+1):
    if(i <= j):
      dp[i][j] = dp[i-1][j] + dp[i][j-i];
    if(j - M - 1 >= 0):
      dp[i][j] -= dp[i-1][j-M-1];
    dp[i][j] = dp[i][j] % mod;

print(dp)
print(dp[-1][-1] % 100000)
