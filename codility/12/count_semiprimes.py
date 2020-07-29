from math import gcd

def solution(A,B):
  N = len(A)
  count = 0
  for i in range(N):
    g = gcd(A[i],B[i])

    a = A[i]
    while a >= 1:
      d = gcd(g,a)
      if d == 1: break
      a //= d

    b = B[i]
    while b >= 1:
      d = gcd(g,b)
      if d == 1: break
      b//= d

    count += 1 if a==1 and b==1 else 0

  return count


print(solution([15,10,3],[75,30,5]))