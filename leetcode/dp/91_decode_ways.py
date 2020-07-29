class Solution:
    def numDecodings(self, s: str) -> int:
        
        # memo = {}
        # def helper(i):
        #     if i in memo:
        #         return memo[i]

        #     if i == len(s):
        #         return 1

        #     if i > len(s) or int(s[i]) == 0:
        #         return 0

        #     if 10 <= int(s[i:i+2]) <= 26:
        #         memo[i] = helper(i+1) + helper(i+2)
        #         return memo[i]
        #     else:
        #         memo[i] = helper(i+1)
        #         return memo[i]

        # return helper(0)

        dp = [0] * (len(s)+1)
        dp[-1] = 1
        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
                if i+1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]

        return dp[0]

print(Solution().numDecodings("226"))

print(Solution().numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
