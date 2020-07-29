
# # top-down
# def rec(l,r):
#   print(l,r)
#   if dp[l][r] != -1: return dp[l][r]
#   if abs(l-r) <= 1: return 0

#   res = 0
#   # pattern1: create a pair of (l,r)
#   if abs(A[l]-A[r-1])<=1 and rec(l+1,r-1)==r-l-2:
#     res = r - 1

#   # patter2: separate interval
#   for mid in range(l+1, r-1):
#     res = max(res, rec(l,mid)+rec(mid,r) )

#   dp[l][r] = res
#   return res

# while True:
#   N = int(input())
#   if N==0: exit()
#   A = list(map(int,input().split()))
#   dp = [ [0]*N for _ in range(N) ]

#   # Wは2から
#   for W in range(2,N+1): 
#     for i in range(N-W+1): 
#       j = i+W-1

#       if (W-2)%2==0:
#         if dp[i+1][j-1]==W-2 and abs(A[i]-A[j])<=1:
#           dp[i][j] = W
#           continue

#       for k in range(i,j):
#         dp[i][j] = max(dp[i][j], dp[i][k]+dp[k+1][j])

#   print(dp[0][-1])


### [l, r) : rは含まない
while True:
  N = int(input())
  if N==0: exit()
  A = list(map(int,input().split()))
  dp = [ [0]*(N+1) for _ in range(N+1) ]

  # Wは2から
  for W in range(2,N+1): 
    for i in range(N-W+1): 
      j = i+W
      if (W-2)%2==0:
        if dp[i+1][j-1]==W-2 and abs(A[i]-A[j-1])<=1:
          dp[i][j] = W
          continue

      for k in range(i+1,j):
        dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j])

  for m in dp: print(m)
  print(dp[0][N])


# def main(n):
#     a = list(map(int, input().split()))
#     dp = [[0] * (n+1) for i in range(n)]
#     # 区間[l,r)の最大落とせる個数
#     for i in range(n - 1):
#         if abs(a[i] - a[i + 1]) <= 1:
#             dp[i][i + 2] = 2
#             # 隣り合う達磨weightが1以内のペアをdpに記録
#     for i in range(2, n): # 区間の広さ, 最大で0番目とn-1番目の差
#         for l in range(n-i): # 左側のとれる値は区間の広さに依存
#             r = i+l+1 # 右側は上記2変数から計
#             if abs(a[l] - a[r-1]) <= 1: # 今見ている左端と右端がweight 1以内の時
#                 if dp[l+1][r-1] == r-l-2: # 左右1個ずつ内側の最大落とせる個数が「全部落とせる」だったとき
#                     dp[l][r] = r-l # dp[l][r]は左右端を追加して記録
#                     continue
#             res = dp[l+1][r-1] # とりあえず現在の左右1個ずつ内側の値を記録
#             for li in range(l+1, r): # lとrの間のどこかで区切って「lから区切り」「区切りからr」までの和を出す
#                 tmp = dp[l][li] + dp[li][r] # 区間[l, li) と 区間[li, r)のdp和
#                 if res < tmp: #区切った場所が最大値を更新するのであればresを更新
#                     res = tmp
#             dp[l][r] = res
#     print(dp[0][n]) # 左端 0 から右端 n-1 までの最大値を出す

# if __name__ == "__main__":
#     while 1:
#         n = int(input())
#         if n:
#             main(n)
#         else:
            # break