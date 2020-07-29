N,M = map(int,input().split())
dist = [0]
MOD = 10**5
for _ in range(N-1):
  d = int(input())
  dist.append(d)

for i in range(N-1):
  dist[i+1] += dist[i]

res = 0
cur = 0
for _ in range(M):
  a = int(input())
  res += abs(dist[cur+a] - dist[cur]) % MOD
  cur = cur+a

print(res%MOD)