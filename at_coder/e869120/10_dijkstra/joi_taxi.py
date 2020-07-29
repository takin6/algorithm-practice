from collections import deque
import heapq

N,K = map(int,input().split())
C,R = [],[]
for _ in range(N):
  c,r = map(int,input().split())
  C.append(c)
  R.append(r)

adj = [ [] for _ in range(N+1) ]
for _ in range(K):
  a,b = map(int,input().split())
  adj[a].append(b)
  adj[b].append(a)

adj2 = [ [] for _ in range(N+1) ]
for i in range(1, N+1):
  q = deque([i])
  steps = 0
  visited = [False] * (N+1)
  neis = set()

  while q and steps < R[i-1]:
    l = len(q)
    next_q = deque([])

    for _ in range(l):
      node = q.popleft()
      visited[node] = True

      for nei in adj[node]:
        if visited[nei]: continue
        if nei in q: continue
        if nei in next_q: continue
        next_q.append(nei)
        neis.add(nei)

    steps += 1
    q = next_q

  for node in neis:
    adj2[i].append((C[i-1], node))

# for i in range(1, N+1):
#   print(adj2[i])

pq = [(0,1)]
dist = [10**19] * (N+1)
visited = [False] * (N+1)
while pq:
  d,n = heapq.heappop(pq)
  visited[n] = True

  for nd,nei in adj2[n]:
    if visited[nei]: continue
    if d+nd < dist[nei]:
      dist[nei] = d+nd
      heapq.heappush(pq, (d+nd, nei))

print(dist[N])