# def LCS(x,y):
#   N,M = len(x),len(y)
#   dp = [ [0]*(M+1) for _ in range(N+1)]

#   for i in range(1, N+1):
#     for j in range(1, M+1):
#       if x[i-1] == y[j-1]:
#         dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]+1)
#       else:
#         dp[i][j] = max(dp[i-1][j], dp[i][j-1])

#   return dp[-1][-1]

def LCS(x,y):
  dp = []
  for ch2 in y:
    bgn_idx = 0
    for i, cur_idx in enumerate(dp):
      chr_idx = x.find(ch2, bgn_idx) + 1
      if not chr_idx:
        break
      dp[i] = min(cur_idx, chr_idx)
      bgn_idx = cur_idx
    else:
      chr_idx = x.find(ch2, bgn_idx) + 1
      if chr_idx:
        dp.append(chr_idx)
    print(dp)

  return len(dp)

N = int(input())
for _ in range(N):
  x = input()
  y = input()
  print(LCS(x,y))