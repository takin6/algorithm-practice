# for i in range(L):
#   x = int(N[i])
#   # ちょうどはらう
#   dp[i+1][0] = min(dp[i][0]+x, dp[i][1]+x)
#   # 1多く払う
#   dp[i+1][1] = min(dp[i][0]+1)

# dp[i][j] = i桁目で繰り下がりが発生したorしないときの、最大

N = input()
L = len(N)
dp = [ [0]*2 for _ in range(L+1)]
N = N[::-1]
dp[0][0] = 0
dp[1][0] = 1

for i in range(1,L+1):
  x = int(N[i-1])
  dp[i][0] = min(x+dp[i-1][0], x+dp[i-1][1])
  if x+1 >= 10:
    dp[i][1] = min(1+(10-x)+dp[i-1][0], 1+(10-x)+dp[i-1][1])
  else:
    dp[i][1] = min(x+1+dp[i-1][0], x+1+dp[i-1][1])
    

print(dp)
print(dp[L][0])