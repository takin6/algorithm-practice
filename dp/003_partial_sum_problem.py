# def partial_sum_problem():
#     n = 3
#     a = [7, 5, 3]
#     A = 10

#     dp = [ [ False for _ in range(20) ] for _ in range(n+1)]

#     for i in range(n):
#       for j in range(A+1):

#         if i == 0 and j == 0: dp[i][j] = True
#         if i == 0 and j != 0: dp[i][j] = False

#         if j >= a[i]:
#           dp[i+1][j] = dp[i][j-a[i]] or dp[i][j]
#         elif j < a[i]:
#           dp[i+1][j] = dp[i][j]

#     print(dp)
#     return dp[n][A]

# print(partial_sum_problem())


# def counting_partial_sum_problem():
#     n = 5
#     a = [7, 5, 3, 1, 8]
#     A = 12

#     dp = [ [ 0 for _ in range(20) ] for _ in range(n+1)]

#     for i in range(n):
#       for j in range(A+1):

#         if i == 0 and j == 0: dp[i][j] = 1
#         if i == 0 and j != 0: dp[i][j] = 0

#         if j >= a[i]:
#           dp[i+1][j] = dp[i][j-a[i]] + dp[i][j]
#         elif j < a[i]:
#           dp[i+1][j] = dp[i][j]

#     print(dp)
#     return dp[n][A]

# print(counting_partial_sum_problem())

def min_count_partial_sum_problem():
    n = 5
    a = [7, 5, 3, 1, 8]
    A = 12

    # n = 2
    # a = [7, 5]
    # A = 6

    INF = 10 ** 32
    dp = [ [ INF for _ in range(20) ] for _ in range(n+1)]

    for i in range(n):
      for j in range(A+1):
        if i == 0 and j == 0: dp[i][j] = 0

        if j >= a[i]:
          dp[i+1][j] = min(dp[i][j-a[i]]+1, dp[i][j])
        else:
          dp[i+1][j] = dp[i][j]

    if dp[n][A] == INF: return -1

    return dp[n][A]

print(min_count_partial_sum_problem())
