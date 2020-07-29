from typing import List
import math
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        LEN = len(A)

        # def helper(row, col):
        #     if row >= LEN or col >= LEN or row < 0 or col < 0:
        #         return float('inf')
        #     if row == LEN-1:
        #         return A[row][col]
            
        #     return min(
        #         A[row][col] + helper(row+1, col), 
        #         A[row][col] + helper(row+1, col+1),
        #         A[row][col] + helper(row+1, col-1)
        #     )

        # ans = float('inf')
        # for i in range(LEN):
        #     ans = min(ans, helper(0, i))
        # return ans

        for i in range(1, LEN):
            for j in range(0, LEN):
                if j == 0:
                    A[i][j] += min(A[i-1][j], A[i-1][j+1])
                elif j == n-1:
                    A[i][j] += min(A[i-1][j], A[i-1][j-1])
                else:
                    A[i][j] += min(A[i-1][j], A[i-1][j-1], A[i-1][j+1])

        return min(A[LEN-1])


print(Solution().minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))