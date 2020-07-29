from collections import deque
n,m = map(int,input().split())
white = 0
maze = []
for _ in range(n):
  row = list(input())
  white += row.count(".")
  maze.append(row)
steps = [ [-1]*m for _ in range(n) ]
steps[0][0] = 0

q = deque([(0,0)])
while q:
  r,c = q.popleft()

  for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
    nr,nc = r+x,c+y
    if nr<0 or nc<0 or nr>=n or nc>=m: continue
    if maze[nr][nc] == "#": continue
    if steps[nr][nc] != -1: continue
    steps[nr][nc] = steps[r][c] + 1
    if nr==n-1 and nc==m-1:
      break
    else:
      q.append((nr,nc))

if steps[n-1][m-1] == -1:
  print(-1)
else:
  print( white - steps[n-1][m-1] - 1)

