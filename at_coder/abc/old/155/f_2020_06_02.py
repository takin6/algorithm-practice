s = input()
s = "".join([ i for i in reversed(s)]) + "0"
 
INF = 10 ** 32
n = len(s)
dp = [ [INF]*2 for _ in range(n)]
 
dp[0][0] = 0
 
for i in range(n-1):
    x = int(s[i])
    dp[i+1][0] = min( dp[i][0]+x, dp[i][1]+x )
    dp[i+1][1] = min( dp[i][0]+1+(10-x), dp[i][1]+(9-x) )
 
print(min(dp[n-1][0], dp[n-1][1]))


# 36
# => 63 (reversed)
# 　　　　0   1 (6)                2 (3)
# そのまま　0   6                    8 (6+3 or 5+3)
# 繰り上げ INF 5 (6 or 5 (10-6)+1)  11 (6+(10-3)+1 or 5+(9-3))