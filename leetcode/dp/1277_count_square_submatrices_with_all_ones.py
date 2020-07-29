from typing import List
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [ [0] * C for _ in range(R) ]

        res = 0
        for i in range(R):
          for j in range(C):
            if matrix[i][j] == 0:
              continue
            elif i == 0 or j == 0:
              if matrix[i][j] == 1:
                dp[i][j] = 1
                res += 1
            else:
              if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                res += dp[i][j]

        return res

print(Solution().countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))