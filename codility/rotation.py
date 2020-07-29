def solution(A, K):
  N = len(A)
  if N == 0:
    return A

  r = K % N
  if r == 0:
    return A

  return A[-r:] + A[:N-r]

# print(solution([3, 8, 9, 7, 6], 3)) 
# print([1, 2, 3, 4], 4)
print([], 0)