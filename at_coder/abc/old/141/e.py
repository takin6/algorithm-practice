# l1 + len <= l2
# S[l1+i] = S[l2+i] (i=0,1,...,len-1)


N = int(input())
S = input()

dp = [ [0] * N for _ in range(N) ]

for i in range(N):
  for j in range(i+1, N):
    if S[i] == S[j]:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)
    else:
      dp[i][j] = max(dp[i][j-1], dp[i-1][j])

ans = 0
for d in dp:
  ans = max(ans, max(d))

print(ans)