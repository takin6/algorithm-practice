# a,b = map(int, input().split())

## recursive solution ##
# def gcdExtended(a,b):
#   if a == 0:
#     return b,0,1

#   gcd,x1,y1 = gcdExtended(b%a, a)
#   x = y1 - (b//a) * x1
#   y = x1

#   return gcd,x,y

def gcdExtended(a,b):
  x0, x1, y0, y1 = 0, 1, 1, 0
  while a != 0:
    (q, a), b = divmod(b,a), a
    y0, y1 = y1, y0 - q * y1
    x0, x1 = x1, x0 - q * x1
  return b, x0, y0

a,b = 35,15
g,x,y = gcdExtended(a,b)
print(g,x,y)

# https://www.youtube.com/watch?v=jhqFJe6-Cnk