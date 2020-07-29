import heapq
N,M = map(int,input().split())
pq = [-i for i in list(map(int,input().split()))]
heapq.heapify(pq)

for _ in range(M):
  i = heapq.heappop(pq)
  i *= -1
  i //= 2
  heapq.heappush(pq, -i)

print(-sum(pq))