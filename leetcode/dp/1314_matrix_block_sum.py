from typing import List
import pprint
def matrixBlockSum(mat: List[List[int]], K: int) -> List[List[int]]:
    # mat[r][c]
    # i - K <= r <= i + K
    # j - k <= c <= j + K
    #(r,c)
    M = len(mat)
    N = len(mat[0])

    dp = [ [0] * (N+1) for _ in range(M+1) ]
    for i in range(1,M+1):
      for j in range(1,N+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) - dp[i-1][j-1] + mat[i-1][j-1]

    answer = [ [0] * (N) for _ in range(M) ]

    for r in range(0, M):
      for c in range(0, N):
        r1, r2 = max(0, r-K), min(r+K, M-1)
        c1, c2 = max(0, c-K), min(c+K, N-1)

        r1, r2, c1, c2 = r1+1, r2+1, c1+1, c2+1
        answer[r][c] = dp[r2][c2] - dp[r2][c1-1] - dp[r1-1][c2] + dp[r1-1][c1-1]


    return answer

print(matrixBlockSum( [[1,2,3],[4,5,6],[7,8,9]], 1))



[[0, 0, 0, 0], 
[0, 1, 3, 6],
[0, 5, 12, 21],
[0, 12, 27, 45]]