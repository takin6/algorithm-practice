n = int(input())
dp = [0] * (n+1)
dp[0] = 1

for i in range(1, n+1):
  if i == 1:
    dp[1] = 1
  else:
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])