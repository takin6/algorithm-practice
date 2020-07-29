k, n = list(map(int, input().split()))
dist = list(map(int, input().split()))
dist.append(k+dist[0])
l = 0

for i in range(n):
  l = max(l, dist[i+1]-dist[i])

print(k - l)