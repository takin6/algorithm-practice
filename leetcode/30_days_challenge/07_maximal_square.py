from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp = [ [0] * len(matrix[0]) for _ in range(len(matrix)) ]
        # maxlen = 0

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i == 0 or j == 0:
        #             dp[i][j] = 1 if dp[i][j] == "1" else 0

        #         if matrix[i][j] == "1":
        #             dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        #             maxlen = max(maxlen, dp[i][j])

        # print(dp)
        # return maxlen * maxlen

        # cols
        dp = [0] * (len(matrix[0]) + 1)
        maxlen = 0
        prev = 0
        for i in range(1, len(matrix)+1):
            for j in range(1, len(matrix[0])+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == "1":
                    dp[j] = min(dp[j-1], prev, dp[j]) + 1
                    maxlen = max(maxlen, dp[j])
                prev = tmp

        return maxlen * maxlen;

print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))