import math
N = int(input())
ints = list(map(int,input().split()))

# 最大公約数 Euclidの互除法
# gcd = great common divisors
def gcd(x,y):
  while x%y != 0:
    x,y = y,x%y
  return y

# finding gcd of multiple numbers
d = ints[0]
for i in range(1, N):
  d = gcd(d, ints[i])

# prints divisors in sorted order
res = []
for i in range(1, int(math.sqrt(d)+1)):
  if d % i == 0:
    if d // i == i:
      print(i)
    else:
      print(i)
      res.append(int(d//i))

for i in res[::-1]: print(i)
