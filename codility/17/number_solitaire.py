

# dp[i] = i番目でゲーム終了する場合の最大スコア
def solution(A):
  MIN_INF = -10**100
  dp = [MIN_INF] * len(A)
  dp[0] = A[0]

  for i in range(len(A)):
    for j in range(1, 7):
      if i+j >= len(A): break
      dp[i+j] = max(dp[i+j], dp[i]+A[i+j])

  return dp[-1]

print(solution([1,-2,0,9,-1,-2]))