# W = int(input())
# N,K = map(int, input().split())
# vals, widths = [], []
# for _ in range(N):
#   width,val = map(int, input().split())
#   vals.append(val)
#   widths.append(width)

# dp = [ [(0,0)] * (W+1) for _ in range(N+1) ]
# res = 0

# for i in range(N):
#   for w in range(W+1):
#     val, pair = dp[i][w]
#     if w >= widths[i]:
#       dp[i+1][w] = max((val,pair), (dp[i][w-widths[i]][0]+vals[i], dp[i][w-widths[i]][1]+1))
#       if dp[i+1][w][1] <= K:
#         res = max(res, dp[i+1][w][0])
#     else:
#       dp[i+1][w] = (val,pair)

# print(res)

# W = int(input())
# N, K = map(int, input().split())
# a, b = ([], [])

# for i in range(N):
#     aa, bb = map(int, input().split())
#     a.append(aa); b.append(bb)

"""
def rec(i, j, k):
    # i 番目以降から j 個選んだ時の選んだ時の最大の価値を返す
    if i >= N:
        return 0
    if j >= K:
        return 0
    ans = 0
    # 入れる
    if k >= a[i]:
        ans = rec(i+1, j+1, k-a[i])+b[i]
    ans = max(rec(i+1, j, k), ans)
    return ans

print(rec(0, 0, W))
"""


#MLE
W = int(input())
N, K = map(int, input().split())
#A=widths
#B=values
A, B = [],[]

for i in range(N):
    aa, bb = map(int, input().split())
    A.append(aa); B.append(bb)

# dp = [[[0 for z in range(W+1)] for y in range(K+1)] for x in range(N+1)]
# #dp[i][j][k] = i番目以下の荷物からj個以下選び、重さkがWを超えないように荷物を選んだ時の
# #価値の最大値

# #dp[i][j][k] = k番目まで調べたときの

for i in range(1, N+1):
  for j in range(1, K+1):
    for k in range(0, W+1):
      if k >= A[i-1]:
        dp[i][j][k] = max(dp[i-1][j-1][k], dp[i-1][j][k], dp[i-1][j-1][k-A[i-1]]+B[i-1])
      else:
        dp[i][j][k] = max(dp[i-1][j-1][k], dp[i-1][j][k])

# print(dp)
print(dp[N][K][W])

# https://ch.nicovideo.jp/yoshiki_utakata/blomaga/ar673852


# W=int(input())
# N,K=map(int, input().split())
 
# # dp=[[12000000 for i in range(5001)] for j in range(51)]
# dp=[[float('inf') for i in range(23)] for j in range(50)]
# dp[0][0] = 0
 
# tot=0
# for i in range(N):
#   A,B=map(int, input().split())
  
#   for x in range(i,-1,-1):
#     for y in range(tot,-1,-1):
#       dp[x+1][y+B] = min(dp[x+1][y+B], dp[x][y]+A)
#   tot += B
 
# ma=0
# for i in range(0,K+1):
#   for j in range(0,50):
#     if dp[i][j]<=W:
#       ma = max(ma,j)
 
# print(dp)
# print(ma)


# # row = vals
# # col = 
# [
# [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
# [inf, 3, inf, inf, inf, 4, 2, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], 
# [inf, inf, inf, inf, inf, inf, 7, 5, 6, inf, inf, 6, 7, 5, inf, inf, inf, inf, inf, inf], 
# [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 9, 10, 8, inf, inf, inf, 9, inf],
# [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 12],
# ]