from typing import List
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # self.step = math.inf
        # def helper(a, s):
        #     if s > self.step: return
        #     if a < 0: return -1
        #     if a == 0: 
        #         self.step = min(self.step, s)
        #         return 1

        #     return [ helper(a-coin, s+1) for coin in coins]

        # helper(amount, 0)
        # return self.step

        # def helper(rem, count):
        #     if rem < 0: return -1
        #     if rem == 0: return 0
        #     if count[rem-1] != 0: return count[rem-1]
        #     minval = math.inf
        #     for coin in coins:
        #         res = helper(rem-coin, count)
        #         if res >= 0 and res < minval:
        #             minval = 1 + res
        #     count[rem-1] = -1 if minval == math.inf else minval

        #     print(count)
        #     return count[rem-1]

        # return helper(amount, [0]*amount)

        dp = [math.inf] * (amount+1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)

        return dp[amount] if dp[amount] != math.inf else -1      

print(Solution().coinChange([1,2,5],11))
print(Solution().coinChange([2], 3))