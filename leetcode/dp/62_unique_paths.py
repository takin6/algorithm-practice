class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # def helper(i, j):
        #     if i == m-1 and j == n-1:
        #         return 1
        #     if i >= m or j >= n:
        #         return 0

        #     return helper(i, j+1) + helper(i+1, j)

        # return helper(0, 0)

        dp = [ [1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

print(Solution().uniquePaths(3,2))
print(Solution().uniquePaths(7,3))