from collections import deque
H,W,N = map(int,input().split())
graph = []
S = None
for i in range(H):
  row = list(input())
  if "S" in row:
    s = row.index("S")
    S = (i,s)
  graph.append(row)

def bfs(S, target):
  q = deque([S])
  visited = set()
  step = 0

  while q:
    l = len(q)
    next_q = deque()

    for _ in range(l):
      r,c = q.popleft()
      if graph[r][c] == str(target):
        return step, r, c
      visited.add((r,c))

      for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
        nr,nc = r+x,c+y
        if nr<0 or nc<0 or nr>=H or nc>=W: continue
        if (nr,nc) in visited: continue
        if (nr,nc) in next_q: continue
        if graph[nr][nc] == target:
          return step+1, nr, nc
        if graph[nr][nc] != "X":
          next_q.append((nr,nc))

    step += 1
    q = next_q

res = 0
for i in range(1, N+1):
  steps, x,y = bfs(S, i)
  S = (x,y)
  res += steps
  # print(i, steps, (x,y))

print(res)


