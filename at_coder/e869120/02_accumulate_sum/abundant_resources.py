N = int(input())
A = [0]+list(map(int,input().split()))
for i in range(N):
  A[i+1] += A[i]

for i in range(1, N+1):
  res = 0
  for j in range(N-i+1):
    res = max(res, A[j+i]-A[j])
  print(res)

