# def maximum_sum_problem(n):
#   MIN_INF = -10 * 32
#   dp = [ MIN_INF for _ in range(len(n)+1) ]

#   dp[0] = 0

#   for i in range(len(n)):
#     dp[i+1] = max(dp[i], dp[i]+n[i])

#   return dp[-1]

# print(maximum_sum_problem([7,-6,9]))
# print(maximum_sum_problem([-9,-16]))


n = 3
a = [7, -6, 9]