# N
# 1=N
# i => Ai
# 順番

# 3
# 1: 2
# 2: 3
# 3: 1
import heapq

N = int(input())
A = list(map(int,input().split()))

pq = []
for i,a in enumerate(A):
  heapq.heappush(pq,(a,i+1))

for i in range(N):
  print(heapq.heappop(pq)[1], end=" ")