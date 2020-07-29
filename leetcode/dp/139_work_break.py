from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # def helper(i, subs):
        #     print(subs)
        #     if (i,subs) in memo:
        #         return memo[(i,subs)]

        #     if len(subs) == 0: 
        #         return True
        #     if i > len(s): return False

        #     if subs[:i] in wordDict:
        #         return helper(i+1, subs) or helper(0, subs[i:])
        #     else:
        #         return helper(i+1, subs)

        # # print(memo)
        # return helper(0, s)

        # memo = {}
        # def helper(i, subs):
        #     if (i,subs) in memo:
        #         return memo[(i,subs)]

        #     if len(subs) == 0: 
        #         return True
        #     if i > len(s): return False

        #     if subs[:i] in wordDict:
        #         memo[(i+1, subs)] = helper(i+1, subs)
        #         memo[(0, subs[i:])] = helper(0, subs[i:])
        #         return memo[(i+1, subs)] or memo[(0, subs[i:])]
        #     else:
        #         memo[(i+1, subs)] = helper(i+1, subs)
        #         return memo[(i+1, subs)]

        # return helper(0, s)

        # dp - bottom up
        dp = [False] * (len(s)+1)
        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[len(s)]

        


print(Solution().wordBreak("leetcode", ["leet", "code"]))
print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))