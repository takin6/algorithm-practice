# planks: len(A) == len(B) == N
# nails: len(C) == M
# C is an integer within the range [1..2*M];

def ok(m, A, B, C):
  N, M = len(A), len(C)

  # cumulative sum
  cusum = [0] * (2*M+1)
  # add 1 to the position of nail from 0..m

  for i in range(m):
    cusum[C[i]] += 1

  # for every position from 1, create accumulate sum
  # of nails
  for i in range(1, 2*M+1):
    cusum[i] += cusum[i-1]

  # for every plank, check if same # of nails is 
  # positioned??
  # => the # of nails have to be different from 
  #    the start of plank and the end of plank
  for i in range(N):
    # check the difference of the # number of nails between
    # before nail is nailed and after nail is nailed
    if cusum[A[i]-1] == cusum[B[i]]:
      return False

  return True

def solution(A, B, C):
  l, r = 0, len(C)
  res = -1

  # = is needed because we need to update r always
  while r >= l:
    # expected nail counts
    m = (l+r)//2

    if ok(m,A,B,C):
      r = m-1
      res = m
    else:
      l = m+1

  if r == 1 and not ok(len(C), A, B, C): return -1
  return res

print(solution([1,4,5,8], [4,5,9,10], [4,6,7,10,2]))
print(solution([1],[2],[2]))