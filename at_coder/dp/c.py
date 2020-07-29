# 3
# 10 40 70
# 20 50 80
# 30 60 90

# n = 3
# a = [
#   [10, 40, 70],
#   [20, 50, 80],
#   [30, 60, 90]
# ]

# n = 1
# a = [[100, 10, 1]]

# n = 7
# a = [
#   [6, 7, 8],
#   [8, 8, 3],
#   [2, 5, 2],
#   [7, 8, 6],
#   [4, 6, 8],
#   [2, 3, 4],
#   [7, 5, 1]
# ]

n = int(input())

a = []
for i in range(n):
  arr = list(map(int, input().split()))
  a.append(arr)

INF = -10 ** 18

dp = [ [INF] * 3 for i in range(0, n+1)]
dp[0] = [0] * 3

# for i in range(1, n):
#   for j in range(0, 3):
#     idx = [0, 1, 2]
#     idx.remove(j)

#     tmp1 = dp[i-1][j] + a[i][idx[0]]
#     tmp2 = dp[i-1][j] + a[i][idx[1]]
#     dp[i][j] = max(tmp1, tmp2)

#     # chmax(dp[ i + 1 ][ k ], dp[ i ][ j ] + a[ i ][ k ])

#     print(dp)

for i in range(0, n):
  for j in range(0, 3):
    for k in range(3):
      if (j == k): continue
      dp[i+1][k] = max(dp[i+1][k], dp[i][j] + a[i][k])

print(max(dp[-1]))

# for i in range(0, n):
