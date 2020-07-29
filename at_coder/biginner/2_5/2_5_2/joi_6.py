from heapq import heappush,heappop
from collections import defaultdict

INF = 10**100
def dijkstra(s,d,N):
  visited = [False]*N
  times = [INF]*N

  pq = [(s,0)]
  while pq:
    n,t = heappop(pq)
    for nei,nt in adj_list[n]:
      if visited[nei]: continue
      if t+nt < times[nei]:
        times[nei] = t+nt
        heappush(pq, (nei,t+nt))
  return times

N,K = map(int, input().split())
adj_list = defaultdict(list)

for _ in range(K):
  param = list(map(int, input().split()))
  if param[0] == 0:
    s,d = param[1]-1,param[2]-1
    if not adj_list[s]:
      print(-1)
    else:
      times = dijkstra(s,d,N)
      if times[d] == INF:
        print(-1)
      else:
        print(times[d])
  else:
    u,v,t = param[1]-1,param[2]-1,param[3]
    adj_list[u].append((v,t))
    adj_list[v].append((u,t))
