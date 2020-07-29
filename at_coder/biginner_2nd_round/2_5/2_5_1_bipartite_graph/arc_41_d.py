# 頂点はどのタイミングで引き返しても良い！！！

from collections import deque
N,M = map(int,input().split())
adj = [ [] for _ in range(N) ]
for _ in range(M):
  a,b,c = map(str,input().split())
  a = int(a) - 1 
  b = int(b) - 1
  c = 1 if c=="r" else 0
  adj[a].append((b,c))
  adj[b].append((a,c))


def bfs(n, c):
  color = [None] * N
  q = deque([(n,-1,c)])
  cnt = 0

  while q:
    n,p,c = q.popleft()
    if color[n] is None:
      color[n] = c
    else:
      if color[n] == c: continue
      #奇数長のサイクルを発見
      if color[n] == 1-c: return True

    for nei, nc in adj[n]:
      if nei != n and nei != p and nc == c:
        q.append((nei,n,1-c))
        cnt += 1

  return cnt == M

for i in range(N):
  for c in range(2):
    if bfs(i, c):
      print("Yes")
      exit()

print("No")
