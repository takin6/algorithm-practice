class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [ [0] * N for _ in range(N) ]
        for i in range(N):
            dp[i][i] = 1

        res = N

        for i in range(N-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                res += 1
  
        for l in range(2, N):
            for row in range(N-l):
                col = l + row

                if s[row] == s[col] and dp[row+1][col-1] == 1:
                    res += 1
                    dp[row][col] = 1

        return res


print(Solution().countSubstrings("abc"))
