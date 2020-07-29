# import heapq
# N,M = map(int,input().split())
# jobs = []
# for _ in range(N):
#   j = list(map(int,input().split()))
#   if j[0] > M: continue
#   jobs.append(((-j[1],-j[0]), j[0]))
# heapq.heapify(jobs)

# res = 0
# for d in range(M):
#   while jobs:
#     t,i = heapq.heappop(jobs)
#     s,_ = t
#     if d+i <= M:
#       res += -s
#       break

# print(res)

import heapq
N,M = map(int,input().split())
jobs = [ [] for _ in range(M+1) ]
for _ in range(N):
  a,b = map(int,input().split())
  if a <= M:
    jobs[a].append(b)

pq = []
d = 1
res = 0
for _ in range(M-1, -1, -1):
  for b in jobs[d]:
    heapq.heappush(pq, -b)
  if pq:
    res += -heapq.heappop(pq)
  d += 1

print(res)