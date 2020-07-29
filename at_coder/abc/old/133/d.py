# 一か所決めれば他が決まる

N = int(input())
A = list(map(int,input().split()))

x1 = 0
for i,a in enumerate(A):
  if (i&1):
    x1 -= a
  else:
    x1 += a
x1 //= 2

res = [0] * N
res[0] = x1
for i in range(N-1):
  res[i+1] = A[i] - res[i]
for i in range(N):
  res[i] *= 2

print(" ".join(map(str, res)))
