# import sys
# input=lambda: sys.stdin.readline().rstrip()
# n,s,k=map(int,input().split())
# mod=10**9+7
# s-=n*(n-1)//2*k
# if s<0:
#   print(0)
# else:
#   DP=[1]*(s+1) #n=1の場合にi円払う場合の数をDP[i]とする
#   for i in range(2,n+1): #配列を使いまわして先頭に人を追加して人数を増やしていく
#     for j in range(i,s+1): #金額が小さいほうから更新、追加した人が０円の場合と１円以上の場合の和になる
#       DP[j]=(DP[j]+DP[j-i])%mod #１円以上の場合はDP[j-k*i]のkにわたる和になるが、既に更新されており和になっているのでそのまま足せばOK
#       print(i,j,DP)
#   print(DP[s])

n,s,k = map(int, input().split())
mod = 10**9+7
s -= (n*(n-1)//2)*k
if s < 0:
  print(0)
  exit()

dp = [ [1]*(s+1) for _ in range(n+1) ]

for i in range(2, n+1):
  for j in range(s+1):
    if j >= i:
      dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % mod
    else:
      dp[i][j] = (dp[i-1][j]) % mod

print(dp[-1][-1])



# [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
# [0, 0, 1, 0, 1, 1, 1, 1, 2, 1, 2],
# [0, 0, 0, 1, 1, 2, 3, 4, 5, 7, 8],
