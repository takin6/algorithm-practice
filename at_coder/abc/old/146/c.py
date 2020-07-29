# N => A*N + B*d(N)
# N => 10*9 + 10*9*11 = 
A,B,X = map(int,input().split())

# binary search
l,r = 0,10**9+1

while r-l > 1:
  m = (l+r)//2
  d = len(str(m))
  if (A*m + B*d) > X:
    r = m
  else:
    l = m

print(l)

# 49999999994
# 1000000000