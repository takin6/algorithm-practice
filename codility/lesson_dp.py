
# val(A,S) = sum( abs( [ A[i]*S[i] for i in range(N)] ))

# A = [1,5,2,-2]
# # S = {-1,1-1,1}
# S = [-1,1,-1,1]
# N = len(A)

# for i in range(N):
#   print(A[i]*S[i])

# (Assume that the sum of zero elements equals zero.)


def solution(A):
    A = [ abs(i) for i in A ]
    N = len(A)
    dp = [ [float("inf")]*(N+1) for _ in range(2)]
    dp[0][0], dp[1][0] = 0, 0
    # i = 0 (-1), 1(1)
    # dp[i][j]
    for i in range(1, N+1):
        dp[0][i] = min( abs( (A[i-1] * -1) + dp[0][i-1] ), abs( (A[i-1] * -1) + dp[1][i-1] ) )
        dp[1][i] = min( abs( A[i-1] + dp[0][i-1] ), abs( A[i-1] + dp[1][i-1] ) )

#     for i in range(1, N+1):
#         if abs((A[i-1] * -1) + dp[0][i-1]) > abs((A[i-1] * -1) + dp[1][i-1]):
#             dp[0][i] = (A[i-1] * -1) + dp[1][i-1]
#         else:
#             dp[0][i] = (A[i-1] * -1) + dp[0][i-1]

#         if abs(A[i-1] + dp[0][i-1]) > abs(A[i-1] + dp[1][i-1] ):
#             dp[1][i] = A[i-1] + dp[1][i-1]
#         else:
#             dp[1][i] = A[i-1] + dp[0][i-1]
    print(dp)
    return min(abs(dp[0][-1]), abs(dp[1][-1]))


def solution(A):
  N = len(A)
  M = 0
  for i in range(N):
    A[i] = abs(A[i])
    M = max(A[i], M)
  S = sum(A)

  count = [0] * (M+1)
  for i in range(N):
    count[A[i]] += 1

  dp = [-1] * (S+1)
  dp[0] = 0
  for a in range(1, M+1):
    if count[a] > 0:
      for j in range(S):
        if dp[j] >= 0:
          dp[j] = count[a]
        elif j >= a and dp[j-1] > 0:
          dp[j] = dp[j-a] - 1

  print(dp)
  result = S
  for i in range(S//2+1):
    if dp[i] >= 0:
      result = min(result, S-2*i)

  return result

print(solution([1,5,2,-2]))
print(solution([1,5,2,-3]))