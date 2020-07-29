# W = total width
# K = maximum # of screen shots
# a,b = width,importance

# maximize importance
# dp[i][w][k] = i番目までのものから、k個選んだ時に長さをwとするときの最大価値
W = int(input())
N,K = map(int, input().split())
widths,vals = [], []
for _ in range(N):
  w,v = map(int,input().split())
  widths.append(w)
  vals.append(v)

# dp[k][w] = k枚まで使った時の幅がwとなる最大価値
INF = float('inf')
dp = [ [-INF]*(W+1) for _ in range(K+1)]
dp[0][0] = 0

for i in range(N):

  for k in range(K, 0, -1):
    # for w in range(W, 0, -1):
    for w in range(W+1):
      if w >= widths[i] and dp[k-1][w-widths[i]] >= 0:
        dp[k][w] = max(dp[k][w], dp[k-1][w], dp[k-1][w-widths[i]]+vals[i])
      else:
        # dp[k][w] = max(dp[k][w], dp[k-1][w], dp[k][w-1])
        dp[k][w] = max(dp[k][w], dp[k-1][w])

print(max(dp[-1]))

### MLE ###
# dp[i][w][k] = i番目までのものから、k個選んだ時に長さをwとするときの最大価値
# dp = [ [ [0]*(K+1) for _ in range(W+1) ] for _ in range(N+1) ]

# for i in range(1, N+1):
#   for w in range(W+1):
#     for k in range(1,K+1):
#       if w >= widths[i-1]:
#         dp[i][w][k] = max(dp[i-1][w][k], dp[i-1][w-widths[i-1]][k-1]+vals[i-1])
#       else:
#         dp[i][w][k] = max(dp[i-1][w][k], dp[i][w-1][k])

# print(max(dp[-1][-1]))
