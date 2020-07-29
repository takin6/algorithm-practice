from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [ [0] * N for i in range(M)]

        for i in range(M):
            dp[i][0] = 1 if obstacleGrid[i][0] == 0 else 0
        for j in range(N):
            dp[0][j] = 1 if obstacleGrid[0][j] == 0 else 0
        dp[0][0] = 0

        for r in range(1, M):
            for c in range(1, N):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1])

        print(dp)
        return dp[M-1][N-1]
        # for l in range(2, M):
        #     for row in range()

print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))