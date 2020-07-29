class Solution:
    def __init__(self):
        self.count = 0

    def climbStairs(self, n: int) -> int:
        # ----- brute force ----------
        # def helper(i, n):
        #     if i > n: return 0
        #     if i == n: return 1
        #     return helper(i+1, n) + helper(i+2, n)

        # return helper(0, n)

        # ----- memoization -------
        # def helper(i, n, memo):
        #     if i > n: return 0
        #     if i == n: return 1
        #     if memo[i] > 0: return memo[i]
        #     memo[i] = helper(i+1, n, memo) + helper(i+2, n, memo)
        #     return memo[i]

        # return helper(0, n, [0]*100)

        # ------ dp ---------
        MIN_INF = -50000
        dp = [ MIN_INF for _ in range(5000)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

print(Solution().climbStairs(35))
# print(Solution().climbStairs(30))
# print(Solution().climbStairs(2))
print(Solution().climbStairs(3))