class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        N = len(s)
        dp = [ [0] * N for _ in range(N)]

        for i in range(N):
            dp[i][i] = 1

        for b in range(2, len(s)+1):
            for i in range(N-b+1):
                j = i+b-1

                if b == 2:
                    dp[i][j] = 2 if s[i] == s[j] else 1
                    continue

                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                elif s[i] != s[j]:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][N-1]

print(Solution().longestPalindromeSubseq("bbbab"))