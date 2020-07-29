
# dp[i][j][k] = i桁目まで決定、N未満フラグがあるか、3の倍数か？
# 各けたの数字の和が3の倍数であれば、その数字は3の倍数
# = intuition =
# (a+b+c)%x == a%x + b%x + c%x
# - j=1 => not below the current number,
# - j=0 => below the current number
# 10%3 = 1 or 2 or 0

# 未満フラグ = 今見ている状態にまとめられている整数が N 未満であることが確定したか否かを表す Boolean 

D = int(input())
N = input()
L = len(N)
dp = [ [ [0]*D for _ in range(2) ] for _ in range(L+1) ]
dp[0][0][0] = 1
mod = 1000000007

for i in range(L):
  n = int(N[i])
  for j in range(2):
    # 今までの桁を割った数のあまり
    for k in range(D):
      for d in range(10 if j else n+1):
        dp[i+1][j or d<n][(k+d)%D] += dp[i][j][k]
        dp[i+1][j or d<n][(k+d)%D] %= mod

print(dp[L][0][0] + dp[L][1][0] - 1)

[[[1, 0, 0], [0, 0, 0]], [[0, 1, 0], [1, 0, 0]], [[0, 1, 0], [4, 3, 3]], [[0, 1, 0], [34, 33, 33]]]