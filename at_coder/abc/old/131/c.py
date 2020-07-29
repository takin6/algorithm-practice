def gcd(x,y):
  while y:
    x,y = y,x%y
  return x

def calc(x,a,b,l):
  return x - (x//a) - (x//b) + (x//l)

A,B,C,D = map(int,input().split())
lcm = C*D // gcd(C,D)
print(calc(B,C,D,lcm) - calc(A-1,C,D,lcm))

