
### nの分割数を求める方法 ###
# ex) (0,0,5), (0,1,4), (0,2,3) ...
# P(n)を求める方法
# https://www.youtube.com/watch?v=3hc-Urx4S8g
# def integer_partition(n):
#   # dp[i][j] = 1~iでjを作る方法
#   # iを含まずにjを作る方法 & iを含んでjを作る方法=>dp(i, j-i)
#   # if j>=i: dp[i][j] = dp[i-1][j] + dp[i][j-i]
#   dp = [ [0]*(n+1) for _ in range(n+1)]
#   for i in range(n+1):
#     dp[i][0] = 1

#   for i in range(1, n+1):
#     for j in range(1, n+1):
#       if j >= i:
#         dp[i][j] = dp[i-1][j] + dp[i][j-i]
#       else:
#         dp[i][j] = dp[i-1][j]
#   return dp[-1][-1]

# print(integer_partition(5))

### nをk個の分割数にまとめる方法 ###
# P(n,k)を求める方法（NをK分割）
# => 実際自分で書いてみるP(7,2) = P(5,1)=P(6,1) + P(5,2)
# => P(n,k) = P(n-1,k) + P(n-k,k)
# => dpでやるときは、P(k,n)となるので要注意。
# => dp[i][j] = jをi分割した時の数
def pnk(S,N):
  mod = 10**9+7
  dp = [ [1]*(S+1) for _ in range(N+1) ]
  for i in range(2, N+1):
    for j in range(S+1):
      if j >= i:
        dp[i][j] = (dp[i-1][j]+dp[i][j-i]) % mod
      else:
        dp[i][j] = dp[i-1][j] % mod

  return dp[-1][-1]

N,S,K = map(int,input().split())
S = S - (N*(N-1)//2)*K
if S < 0:
  print(0)
else:
  print(pnk(S,N))

# http://www.nct9.ne.jp/m_hiroi/puzzle/partition.html