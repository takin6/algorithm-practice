def LCS():
  # S = "abcde"
  # T = "abcef"

  S = "pirikapirirara"
  T = "poporinapeperuto"
  # => ppriar

  # MIN_INF = -10 ** 32
  dp = [ [ 0 for _ in range(17) ] for _ in range(len(S)+1) ]

  for i in range(len(S)):
    for j in range(len(T)):

      if i == 0 and j == 0: dp[i][j] = 0
      if i == 0 and j != 0: dp[i][j] = 0

      # if i == 11 and j == 7: import pdb; pdb.set_trace()
      if S[i] == T[j]:
        dp[i+1][j+1] = max(dp[i][j]+1, dp[i][j+1], dp[i+1][j])
      else:
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

      # print(dp)

  return dp[len(S)][len(T)]


print(LCS())