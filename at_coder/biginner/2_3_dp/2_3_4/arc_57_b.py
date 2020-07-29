N,K = map(int, input().split())
A = [0]*(N)
cumsum = [0]*(N+1)
dp = [ [float('inf')]*(N+1) for _ in range(N+1) ]

for i in range(N):
  it = int(input())
  dp[i][0] = 0
  A[i] = it
  cumsum[i+1] = cumsum[i]+it
dp[1][1] = 1

if cumsum[N] == K or N == 1:
  print(1)
  exit()

if K == 0:
  print(0)
  exit()

for i in range(1, N):
  a = A[i]
  for j in range(0, i+1):
    dp[i+1][j] = min(dp[i][j], dp[i+1][j])

    x = (dp[i][j]*a // cumsum[i]) + 1
    # if x + dp[i][j] <= K:
    dp[i+1][j+1] = min(dp[i+1][j+1], dp[i][j]+x)

for j in range(N, -1, -1):
  if dp[N][j] <= K:
    print(j)
    break
else:
  print(0)

# print(dp[-1].index(max(dp[-1]))-1)

# acにならない。。。
# 参考
# https://atcoder.jp/contests/arc057/submissions/9033776