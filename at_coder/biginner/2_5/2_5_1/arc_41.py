import sys
sys.setrecursionlimit(100000)

from collections import defaultdict, deque
N,M = map(int, input().split())
adj_list = defaultdict(list)

for _ in range(M):
  a,b,c = map(str, input().split())
  a,b = int(a), int(b)
  c = 1 if c =="r" else 0
  adj_list[a].append((b,c))
  adj_list[b].append((a,c))

def bfs(n, c, p):
  color = [None]*N
  q = deque([(n,-1,c)])
  cnt = 0

  while q:
    n,p,c = q.popleft()
    if color[n-1] is None:
      color[n-1] = c
    else:
      if color[n-1] == c: continue
      # cycle found
      if color[n-1] != c: return True

    for nei,nc in adj_list[n]:
      if nei != n and nei != p and nc == c:
        q.append((nei,n,1-c))
        cnt += 1

  # all coloring succeeded
  if cnt == M:
    return True
  else:
    return False

for i in range(1, N+1):
  for c in range(2):
    if bfs(i, c, -1):
      print("Yes")
      exit()
print("No")