N,M = map(int,input().split())
A = [0] * (N+2)
for _ in range(M):
  l,r = map(int,input().split())
  A[l] += 1
  A[r+1] -= 1

for i in range(N):
  A[i+1] += A[i]

print(A.count(M))