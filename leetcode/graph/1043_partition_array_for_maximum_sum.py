from typing import List

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:

        # N = len(A)
        # dp = [0] * (N + 1)
        # for i in range(N):
        #     curMax = 0
        #     # 1, 2, 3
        #     # dp=[1,30,45,...]
        #     for k in range(1, min(K, i + 1) + 1):
        #         # i = 3
        #         # A[i-k+1] => A[3-1+1] => 9
        #         #             A[3-2+1] => 7
        #         #             A[3-3+1] => 15
        #         curMax = max(curMax, A[i - k + 1])
        #         print(curMax)
        #         print(i, k, dp[i], dp[i - k] + curMax * k)
        #         # i = 3
        #         # dp[i-k]+curMax*k => dp[3-1]+9*1=>45+9=54
        #         #                     dp[3-2]+7*2=>30+7=37
        #         #                     dp[3-3]+15*3=>1+45=45
        #         dp[i] = max(dp[i], dp[i - k] + curMax * k)
        #         print(dp)
        # return dp[N - 1]

        N = len(A)
        dp = [0] * (N+1)

        for i in range(N):
            curMax = 0

            for k in range(1, min(K, i+1)+1):
                curMax = max(curMax, A[i-k+1])
                dp[i] = max(dp[i], dp[i-k]+curMax*k)

        return dp[N-1]

# print(Solution().maxSumAfterPartitioning([1, 15, 7, 9, 2, 5, 10], 3))
print(Solution().maxSumAfterPartitioning([3,7], 2))