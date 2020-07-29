def gcd(x,y):
  x,y = max(x,y),min(x,y)
  while x%y != 0:
    x,y = y,x%y
  return y

def lcm(x,y):
  # x*y = lcm(x,y) *gcd(x,y)
  return x*y // gcd(x,y)

N = int(input())
lst = []
res = None 
for _ in range(N):
  n = int(input())
  if res is None:
    res = n
  else:
    res = lcm(res, n)

print(res)