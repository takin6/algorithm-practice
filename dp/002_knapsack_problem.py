# simple dp solution
def knapsack():
  n = 6
  weight = [2, 1, 3, 2, 1, 5]
  value = [3, 2, 6, 1, 3, 85]
  w = 9

  # import pdb; pdb.set_trace()
  dp = [ [ -10 ** 32 for _ in range(9+1) ] for _ in range(n+1) ]
  dp[0][0] = 0

  for i in range(n):
    for w in range(w+1):

      if i == 0 or weight == 0: dp[i][w] = 0

      if w >= weight[i]:
        dp[i+1][w] = max( dp[i][w-weight[i]]+value[i], dp[i][w])
      elif w < weight[i]:
        dp[i+1][w] = dp[i][w]

  print(dp)
  return dp[n][w]

print(knapsack())