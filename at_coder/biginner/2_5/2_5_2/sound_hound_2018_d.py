from collections import defaultdict
import heapq
INF = 10**100

def dijkstra(N, s, i):
  visited = [False]*(N+1)
  costs = [INF]*(N)
  costs[s-1] = 0

  pq = [(0,s)]
  while pq:
    c, n = heapq.heappop(pq)
    visited[n] = True
    for nei,*fee in adj_list[n]:
      if visited[nei]: continue
      if c+fee[i] < costs[nei-1]:
        costs[nei-1] = c+fee[i]
        heapq.heappush(pq, (costs[nei-1],nei))

  return costs

n,m,s,t = map(int, input().split())
adj_list = defaultdict(list)
for _ in range(m):
  u,v,a,b = map(int, input().split())
  adj_list[u].append((v,a,b))
  adj_list[v].append((u,a,b))

yen_costs = dijkstra(n, s, 0)
snk_costs = dijkstra(n, t, 1)
total_costs = list(map(sum, zip(yen_costs, snk_costs)))
comp = INF
res = []
for c in reversed(total_costs):
  if c < comp:
    res.append(int(1e15 - c))
    comp = c
  else:
    res.append(int(1e15 - comp))

print("\n".join(map(str, reversed(res))))

# 999999574976994

# total_costs = list(map(sum, zip(yen_costs, snk_costs)))
# print(total_costs)
# ans = []
# tmp = INF
# for c in reversed(total_costs):
#   tmp = min(tmp, c)
#   ans.append(1e15 - tmp)
# ans.reverse()

# print("\n".join(map(str, ans)))