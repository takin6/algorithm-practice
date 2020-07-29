# import sys
# sys.setrecursionlimit(10**6)

# n = int(input())
# x = input()
# xi = int('0b' + x, 2)
# xc = x.count("1")

# xip = xi % (xc+1)
# if xc-1 == 0:
#   xim = 0
# else:
#   xim = xi % (xc-1)

# def f(u):
#   if u==0: return 0
#   m = u % bin(u).count("1")
#   return 1 + f(m)

# for i in range(n):
#   if x[i] == "0":
#     y = xip + pow(2, n-i-1, xc+1)
#     y = y % (xc+1)
#   elif xc == 1:
#     print(0)
#     continue
#   else:
#     y = xim - pow(2, n-i-1, xc-1)
#     y = y % (xc-1)

#   print(f(y)+1)

N = int(input())
X = input()
val = int(X,2)
C = X.count("1")

if C==1:
  for i in range(N):
    if X[i]=='1':
      print(0)
    elif i==N-1:
      print(2)
    else:
      print(1)
  exit()

# xをpopcountで割ったあまりに置き換える
def f(x):
  if x==0: return 0
  return 1 + f(x % bin(x).count("1"))

# 初回のpopcountでの割り方は、(C+1) or (C-1)
Y = val%(C+1)
if C-1 != 0:
  Z = val%(C-1)
else:
  Z = 0

for i in range(N):
  if X[i] == "1":
    if Z - 1 <= 0:
      print(0)
      continue
    k = (Z - pow(2,N-i-1,C-1)) % (C-1)
  else:
    k = (Y + pow(2,N-i-1,C+1)) % (C+1)
  print(f(k)+1)