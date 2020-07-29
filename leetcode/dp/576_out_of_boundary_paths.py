class Solution:
    # def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # if i > (m-1) or i < 0 or j < 0 or j > (n-1):
        #     return 1

        # if N == 0:
        #     return 0


    #     return self.findPaths(m, n, N-1, i+1, j) + self.findPaths(m, n, N-1, i-1, j) + self.findPaths(m, n, N-1, i, j+1) + self.findPaths(m, n, N-1, i, j-1)      

    # def findPaths(self, m: int, n: int, N: int, i: int, j: int, memo={}) -> int:
    #     if memo.get((i,j, N)):
    #         return memo[(i,j,N)]

    #     if i > (m-1) or i < 0 or j < 0 or j > (n-1):
    #         return 1

    #     if N == 0:
    #         return 0

    #     memo[(i+1, j, N-1)] = self.findPaths(m, n, N-1, i+1, j)
    #     memo[(i-1, j, N-1)] = self.findPaths(m, n, N-1, i-1, j)
    #     memo[(i, j+1, N-1)] = self.findPaths(m, n, N-1, i, j+1)
    #     memo[(i, j-1, N-1)] = self.findPaths(m, n, N-1, i, j-1)
    #     return memo[(i+1, j, N-1)] + memo[(i-1, j, N-1)] + memo[(i, j+1, N-1)] + memo[(i, j-1, N-1)]

    # my memoized solution
    # def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
    #     memo = {}
    #     mod = 10**9 + 7
    #     def helper(N, i, j):
    #         if memo.get((i,j,N)):
    #             return memo[(i,j,N)]

    #         if i > (m-1) or i < 0 or j < 0 or j > (n-1):
    #             return 1

    #         if N == 0:
    #             return 0

    #         memo[(i+1, j, N-1)] = helper(N-1, i+1, j) % mod
    #         memo[(i-1, j, N-1)] = helper(N-1, i-1, j) % mod
    #         memo[(i, j+1, N-1)] = helper(N-1, i, j+1) % mod
    #         memo[(i, j-1, N-1)] = helper(N-1, i, j-1) % mod
    #         return (memo[(i+1, j, N-1)] + memo[(i-1, j, N-1)] + memo[(i, j+1, N-1)] + memo[(i, j-1, N-1)]) % mod

    #     return helper(N, i, j)

    # 50% faster memoized solution
    # def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
    #     memo = collections.defaultdict(int)
    #     mod = 10**9 + 7
    #     def helper(N, i, j):
    #         if (i,j,N) in memo:
    #             return memo[(i,j,N)]
    #         if N == 0: return 0
            
    #         paths = 0
    #         moves = [(1,0), (-1,0), (0,1), (0, -1)]
    #         for x,y in moves:
    #             if i + x >= 0 and i + x < m and j + y >= 0 and j + y < n:
    #                 paths += helper(N-1,i+x,j+y) % mod
    #             else:
    #                 paths += 1

    #         memo[(i,j,N)] = paths
    #         return paths

    #     return helper(N, i, j) % mod

    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        M = 10**9 + 7
        dp = [ [0]*n for _ in range(m)]
        dp[i][j] = 1
        count = 0

        for move in range(1, N+1):
            temp = [ [0]*n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    # if the pos comes to the boundary, add moves
                    if i == m-1:
                        count = (count + dp[i][j]) % M
                    if j == n-1:
                        count = (count + dp[i][j]) % M
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    if j == 0:
                        count = (count + dp[i][j]) % M

                    # add next positions
                    tmp = 0
                    if i > 0:
                        tmp += dp[i-1][j]
                    if i < m-1:
                        tmp += dp[i+1][j]
                    if j > 0:
                        tmp += dp[i][j-1]
                    if j < n-1:
                        tmp += dp[i][j+1]
                    temp[i][j] = tmp % M
            dp = temp

        return count

print(Solution().findPaths(2,2,2,0,0))

# print(Solution().findPaths(1,3,3,0,1))
# print(Solution().findPaths(8,7,16,1,5))
# print(Solution().findPaths(8,50,23,5,26))
