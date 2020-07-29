import heapq

N,K = map(int, input().split())
a,b = [], []
for _ in range(N):
  i,j = map(int, input().split())
  a.append(i)
  b.append(j)

pq = [(e,i) for i,e in enumerate(a)]
heapq.heapify(pq)

res = 0
for _ in range(K):
  t, idx = heapq.heappop(pq)
  res += t
  heapq.heappush(pq, (t+b[idx], idx))

print(res)