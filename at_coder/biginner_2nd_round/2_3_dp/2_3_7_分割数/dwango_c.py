#チームのプレイヤーをキル数の多い順
#（同じ場合デス数の少ない順）
from collections import Counter

N,M = map(int,input().split())
killA = list(map(int,input().split()))
killB = list(map(int,input().split()))
killGroupA = Counter(killA)
killGroupB = Counter(killB)

deathA = sum(killB)
deathB = sum(killA)

# partition number
dp = [ [0]*(1006) for _ in range(1006)]
dp[0][0] = 1
for i in range(1, 1006):
  for j in range(1006):
    if j >= i:
      dp[i][j] = dp[i-1][j] + dp[i][j-i]
    else:
      dp[i][j] = dp[i-1][j]

# dp[i][j] = i番目の人までにjデス振り分けるときの組み合わせの数
dp1 = [ [0]*1006 for _ in range(N+1) ]
i = 0
for v in killGroupA.values():
  i += 1
  for j in range(1, 1001):
    for k in range(j+1):
      dp1[i][j] += (dp1[i-1][k] * dp[killA[i]][j-k])


# 参考になります。。
# https://atcoder.jp/contests/dwacon2018-prelims/submissions/13216510