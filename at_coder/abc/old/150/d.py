import fractions

# least common multiple
def lcm(a,b):
  f = fractions.gcd(a,b)
  return a*b // f

N,m = list(map(int, input().split()))
A = list(map(int,input().split()))
l = A[0]

# a -> a`
for i in range(N):
  if A[i]%2==1:
    print(0)
    exit(0)
  A[i] //= 2

def F(x):
  res = 0
  while x%2==0:
    x //= 2
    res += 1

  return res

t = F(A[0])
for i in range(N):
  if F(A[i]) != t:
    print(0)
    exit(0)
  A[i] >>= t # a[i] /= 2^t
m >>= t

l = 1
for i in range(N):
  l = lcm(l, A[i])
  if l > m:
    print(0)
    exit(0)

m /= l
print(int((m+1) // 2))



