from typing import List
class Solution:
    import math
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [ [0]*len(grid[0]) for _ in range(len(grid)) ]
        dp[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                
                f = 10**1000
                if i-1 >= 0:
                    f = min(f, dp[i-1][j])
                
                if j-1 >= 0:
                    f = min(f, dp[i][j-1])
                
                dp[i][j] = grid[i][j] + f
        
        return dp[len(grid)-1][-1]

print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))