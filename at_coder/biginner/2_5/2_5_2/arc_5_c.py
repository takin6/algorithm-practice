from collections import deque
import sys
sys.setrecursionlimit(100000)

H,W = map(int,input().split())
maze = []
s = None
g = None
for i in range(H):
  row = list(input())
  if "s" in row:
    s = (i,row.index("s"))
  if "g" in row:
    g = (i,row.index("g"))
  maze.append(row)

INF = 10**100

def dfs():
  q = deque([(s[0],s[1],0)])
  visited = [[[False]*3 for _ in range(W)] for _ in range(H)]
  while q:
    h,w,c = q.popleft()
    if (h,w) == g: break
    next_index = [(h-1,w),(h+1,w),(h,w-1),(h,w+1)]
    for nh,nw in next_index:
      if 0 <= nh < H and 0 <= nw < W:
        if c == 2 and maze[nh][nw] == "#": continue

        if maze[nh][nw] == "#":
          if visited[nh][nw][c+1]: continue
          q.append((nh,nw,c+1))
          visited[nh][nw][c+1] = True
        else:
          if visited[nh][nw][c]: continue
          q.append((nh,nw,c))
          visited[nh][nw][c] = True

  for i in range(3):
    if visited[g[0]][g[1]][i]: 
      return True
  return False
    

if dfs():
  print('YES')
else:
  print('NO')
