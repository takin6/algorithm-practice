
# def func(A,B):
#   if B%A == 0:
#     return A*(2*(B//A-1))
#   else:
#     return A*2*(B//A) + func(B%A,A)

# a,b = max(N-X,X),min(N-X,X)
# print(func(a,b))

N,X = map(int,input().split())
res = N
a,b = max(N-X,X),min(N-X,X)

while b:
  q = a // b
  r = a % b
  res += (b*2)*q
  if r == 0: res -= b

  a,b = b,r

print(res)