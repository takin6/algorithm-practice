class Solution:

    # # recursive
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     text1 += "0"
    #     text2 += "0"
    #     def helper(i,j):
    #         if text1[i] == '0' or text2[j] == '0':
    #             return 0

    #         elif text1[i] == text2[j]:
    #             return 1 + helper(i+1, j+1)
    #         else:
    #             return max(helper(i, j+1), helper(i+1, j))

    #     return helper(0, 0)

    # topdown memoization
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     text1 += "0"
    #     text2 += "0"
    #     memo = {}
    #     def helper(i,j):
    #         if (i,j) in memo: return memo[(i,j)]

    #         if text1[i] == '0' or text2[j] == '0':
    #             memo[(i,j)] = 0
    #             return memo[(i,j)]
    #         elif text1[i] == text2[j]:
    #             memo[(i,j)] = 1 + helper(i+1, j+1)
    #             return memo[(i,j)]
    #         else:
    #             memo[(i,j+1)], memo[(i+1,j)] = helper(i, j+1), helper(i+1, j)
    #             return max(memo[(i,j+1)], memo[(i+1,j)])

    #     return helper(0, 0)

    # bottom-up approach
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0] * (len(text2)+1) for _ in range(len(text1)+1)]
        N, M = len(text1), len(text2)

        for i in range(1, N+1):
            for j in range(1, M+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[N][M]

print(Solution().longestCommonSubsequence("abcde", "ace"))
print(Solution().longestCommonSubsequence("abc", "abc"))
print(Solution().longestCommonSubsequence("abc", "def"))