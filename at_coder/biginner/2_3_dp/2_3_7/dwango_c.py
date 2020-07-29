# from collections import Counter
# def solve(var, total, P):
#   L = len(var)
#   dp = [ [0]*(total+1) for _ in range(L+1) ]
#   dp[0][0] = 1
#   for i in range(L):
#     num = var[i]
#     for j in range(total+1):
#       here = dp[i][j]
#       for k in range(j, total+1):
#         dp[i+1][k] += here * P[k-j][num]

#   print(dp)
#   return dp[-1][-1]

# N,M = map(int, input().split())
# killA = list(map(int, input().split()))
# killB = list(map(int, input().split()))

# max_death = max(sum(killA), max(killB))
# p = max(N, M)

# P = [ [1]*(max_death+1) for _ in range(p+1) ]

# for i in range(2, p+1):
#   for j in range(max_death+1):
#     if j >= i:
#       P[i][j] = P[i-1][j] + P[i][j-i]
#     else:
#       P[i][j] = P[i-1][j]


# ans = solve(list(Counter(killA).values()), sum(killB), P)
# ans *= solve(list(Counter(killB).values()), sum(killA), P)
# print(ans)
