def gcd(a,b):
  while a%b != 0:
    a,b = b,a%b
  return b

N,K = map(int, input().split())
A = list(map(int, input().split()))
m = max(A)
if K > m:
  print('IMPOSSIBLE')
  exit()

if K in A:
  print('POSSIBLE')
  exit()

g = A[0]
for i in A[1:]:
  g = gcd(g,i)

if K % g == 0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")
