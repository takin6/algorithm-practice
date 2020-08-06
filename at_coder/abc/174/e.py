N,K = map(int,input().split())

A = list(map(int,input().split()))

def check(x):
  k = 0
  for a in A:
    k += ((a-1) // x)
  return k <= K

ng,ok = 0, 10**9+1

while ok-ng > 1:
  x = (ok+ng)//2

  if check(x):
    ok = x
  else:
    ng = x

print(ok)