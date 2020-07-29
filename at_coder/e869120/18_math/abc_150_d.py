import fractions
import math

N,M = map(int,input().split())
A = list(map(int,input().split()))
A = [ a//2 for a in A ]

flg = True
times = None
for i,a in enumerate(A):
  t = 0
  while a%2==0:
    a //= 2
    t += 1

  if times is None:
    times = t
  else:
    if times != t:
      flg = False
      break
  A[i] = a
M >>= times

if not flg:
  print(0)
  exit()

lcm = 1
for i in range(N):
  lcm = lcm * A[i] // fractions.gcd(lcm, A[i])
  if lcm > M:
    print(0)
    exit()

print(math.ceil((M // lcm)/2))

# lcm = 1
# while len(A) > 1:
#   a,b = A.pop(), A.pop()
#   lcm = a*b // math.gcd(a,b)
#   if lcm > M:
#     print(0)
#     exit()
#   A.append(lcm)

# print(lcm)
# import pdb; pdb.set_trace()
# print(math.ceil((M // lcm)/2))
