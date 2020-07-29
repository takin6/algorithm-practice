K,N = map(int,input().split())
A = list(map(int,input().split()))

cumsum = [0]
for i in range(N):
  cumsum.append(A[i])
for i in range(N):
  cumsum.append(A[i]+K)

res = 10**14
for i in range(N, 2*N):
  res = min(res, cumsum[i]-cumsum[i-N+1])
print(res)
print(cumsum)