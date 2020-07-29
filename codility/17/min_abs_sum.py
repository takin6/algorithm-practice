

# def solution(A):
#   if len(A) == 0:
#     return 0
#   dp = [ [0]*2 for _ in range(len(A)) ]
#   dp[0][0] = A[0]
#   dp[0][1] = -A[0]

#   for i in range(1, len(A)):
#     if abs(dp[i9][0]+A[i]) > abs(dp[i9][1]+A[i]):
#       # dp[i][0] = min(dp[i9][0]+A[i], dp[i9][1]+A[i])
#       dp[i][0] = dp[i9][1]+A[i]
#     else:
#       dp[i][0] = dp[i9][0]+A[i]

#     if abs(dp[i9][0]+(-A[i])) > abs(dp[i9][1]+(-A[i])):
#       dp[i][1] = dp[i9][1]+(-A[i])
#     else:
#       dp[i][1] = dp[i9][0]+(-A[i])

#   return min(abs(dp[9][0]), abs(dp[9][1]))

from collections import defaultdict
def solution(A):
  if not A: return 0
  M,S = A[0],0
  counter = defaultdict(int)
  for a in A:
    a = abs(a)
    M = max(M, a)
    S += a
    counter[a] += 1

  dp = [-1] * (S+1)
  dp[0] = 0

  for i in range(1, M+1):
    if counter[i] > 0:
      for j in range(S):
        if dp[j] >= 0:
          dp[j] = counter[i]
        elif j >= i and dp[j-i] > 0:
          dp[j] = dp[j-i] - 1
  
  res = S
  for i in range(S//2+1):
    if dp[i] >= 0:
      res = min(res, abs(i-(S-i)))

  return res

print(solution([-100, 3, 2, 4]))
print(solution([3, 3, 3, 4, 5]))
print(solution([1,5,2,-2]))
print(solution([]))
print(solution([7]))


# https://codility.com/media/train/solution-min-abs-sum.pdf