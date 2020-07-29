# knapsack = H
# weight = A, value = B
# dp[i][h] = i種類の魔法でモンスターにhのダメージを与える場合の、消費魔力の最小値
# import math
# H, N = list(map(int,input().split()))
# A,B = [None]*N, [None]*N

# for i in range(N):
#   A[i], B[i] = list(map(int,input().split()))

# dp = [ [math.inf]*(N+1) for _ in range(H+1) ]
# dp[0][0] = 0

# for i in range(N):
#   for j in range(H+1):
#     dp[i+1][j] = min(dp[i+1][j], dp[i][j])
#     import pdb; pdb.set_trace()
#     dp[i+1][j] = min(dp[i+1][min(j+A[i], H)], dp[i+1][j]+B[i])

# print(dp[N][H])

# ============================================-
# knapsack = 9, N = 3

# Weight = A, value = B
# 8 3
# 4 2
# 2 1

# dp[i] = monsterの体力をiへ荒らすため消耗する魔力の最小値

# dp[1] = 1
# dp[2] = 1
# dp[3] = 2 == min(dp[1]+)
# dp[4] = 2
# dp[5] = 3
# dp[6] = 3
# dp[7] = 3
# dp[8] = 3
# dp[9] = 4


# dp[i] = monsterの体力をiへ減らすために消耗する魔力の最小値
# H=9
# 8 3
# 4 2
# 2 1
# import math
# H, N = list(map(int,input().split()))
# dp = [math.inf] * (H+1)
# # 0減らすために消耗する魔力の最小値は0
# dp[0] = 0

# for i in range(N):
#   a,b = list(map(int,input().split()))

#   # モンスターの体力がjのとき
#   for j in range(H):
#     # モンスターに与えられるのダメージを計算
#     dmg = min(j+a, H)
#     # damage減らすための
#     dp[dmg] = min(dp[dmg], dp[j]+b)
#   print(i)
#   print(dp)

# H, N = 9, 3
# A = [8,4,2]
# B = [3,2,1]

# H,N = 100,6
# A = [1,2,3,4,5,6]
# B = [1,3,9,27,81,243]

# memo = {}
# def helper(h, hp):
#   if h < 0:
#     return hp

#   return min([ helper(h-A[i], hp+B[i]) for i in range(N) ])

# H, N = 9, 3
# A = [8,4,2]
# B = [3,2,1]
# H,N = 100,6
# A = [1,2,3,4,5,6]
# B = [1,3,9,27,81,243]


# first attempt
# H,N = list(map(int,input().split()))
# A, B = [], []
# for _ in range(N):
#   a,b = list(map(int,input().split()))
#   A.append(a)
#   B.append(b)
# dp = [float("inf")] * (H+1)

# for h in range(1, H+1):
#   for i in range(N):

#       if h - A[i] <= 0:
#           dp[h] = min(dp[h], B[i])
#       else:
#           dp[h] = min(dp[h], B[i] + dp[h - A[i]])

# print(dp[-1])

H,N = list(map(int,input().split()))
dp = [float("inf")] * (H+1)

for i in range(N):
  a,b = list(map(int,input().split()))

  for h in range(1, H+1):
    if h - a <= 0:
      dp[h] = min(dp[h], b)
    else:
      dp[h] = min(dp[h], b + dp[h - a])

print(dp[-1])



# print(helper(H, 0))