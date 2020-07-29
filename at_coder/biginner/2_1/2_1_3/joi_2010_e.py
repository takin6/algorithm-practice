from collections import deque
import sys
readline = sys.stdin.readline

H,W,N = list(map(int, input().split()))
matrix = []
goals = [None] * (N+1)  
for i in range(H):
  row = list(readline().rstrip())

  for j in range(W):
    if row[j] == "S":
      goals[0] = (i,j)
    if row[j].isnumeric():
      goals[int(row[j])] = (i,j)

  matrix.append(row)

def bfs(start, end):
  visited = [[False]*W for _ in range(H)]
  q = deque([(start[0],start[1],0)])

  res = 10**100
  while q:
    r,c,step = q.popleft()
    # visited.append((r,c))

    for y,x in [(1,0),(-1,0),(0,1),(0,-1)]:
      nr,nc = r+y,c+x
      if (nr,nc) == end:
        res = min(res, step+1)
        return res

      if nr<0 or nc<0 or nr>=H or nc>=W: continue
      if visited[nr][nc] or (nr,nc,step+1) in q: continue
      if matrix[nr][nc] != "X":
        visited[nr][nc] = True
        q.append((r+y, c+x, step+1))

  return res

res = 0
for i in range(N):
  res += bfs(goals[i], goals[i+1])
print(res)
