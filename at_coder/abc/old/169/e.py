N = int(input())
A = []
B = []

for _ in range(N):
  a,b = map(int,input().split())
  A.append(a)
  B.append(b)

A.sort()
B.sort()

if N%2==0:
  mA = (A[N//2-1]+A[N//2])/2
  mB = (B[N//2-1]+B[N//2])/2
  print(int((mB - mA)*2 + 1))
else:
  mA = A[N//2]
  mB = B[N//2]
  print(mB-mA+1)