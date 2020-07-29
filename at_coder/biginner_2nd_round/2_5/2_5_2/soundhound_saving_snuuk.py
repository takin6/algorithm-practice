import heapq
N,m,S,T = map(int,input().split())
S -= 1
T -= 1
adj_yen = [ [] for _ in range(N) ]
adj_snk = [ [] for _ in range(N) ]

for _ in range(m):
  u,v,y,sn = map(int,input().split())
  u -= 1
  v -= 1
  adj_yen[u].append((v,y))
  adj_yen[v].append((u,y))

  adj_snk[u].append((v,sn))
  adj_snk[v].append((u,sn))

def dijkstra(g,s):
  costs = [float("inf")] * N
  costs[s] = 0
  visited = [False] * N

  q = [(0,s)]
  while q:
    c,n = heapq.heappop(q)
    if visited[n]: continue
    visited[n] = True

    for nei, nc in g[n]:
      if nc+c < costs[nei]:
        costs[nei] = nc+c
        heapq.heappush(q, (nc+c,nei))
  return costs

costs_yen = dijkstra(adj_yen, S)
costs_snk = dijkstra(adj_snk, T)

cur_year = N-1
prev_cost = 10**15
res = [0] * N
while cur_year >= 0:
  tot = costs_yen[cur_year] + costs_snk[cur_year]
  res[cur_year] = 10**15 - min(prev_cost, tot)
  prev_cost = min(prev_cost, tot)
  cur_year -= 1

for r in res:
  print(r)
