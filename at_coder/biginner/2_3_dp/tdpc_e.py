D = int(input())
N = input()
L = len(N)
MOD = 1000000007

dp = [ [ [0]*D for _ in range(2) ] for i in range(L+1)]
dp[0][0][0] = 1

for i in range(L):
  n = int(N[i])

  for j in range(2):

    for k in range(D):

      for d in range(10 if j else n+1):
        dp[i+1][j or d<n][(k+d)%D] += dp[i][j][k]
        dp[i+1][j or d<n][(k+d)%D] %= MOD

print(dp[L][0][0] + dp[L][1][0]-1 % MOD)

# - intuition
# (a+b+c)%x == a%x + b%x + c%x
# - j=1 => not below the current number,
# - j=0 => below the current number