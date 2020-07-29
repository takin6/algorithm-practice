N, K = list(map(int, input().split()))
p = list(map(int, input().split()))

T = [0] * (N+1)

for i in range(N):
  T[i+1] = T[i] + (1+p[i])/2

ans = 0
for j in range(K, N+1):
  ans = max(ans, T[j]-T[j-K])

print(ans)