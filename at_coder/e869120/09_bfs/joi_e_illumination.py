from collections import deque
W,H = map(int,input().split())
maze = []
maze.append([0]*(W+2))
for i in range(H):
  maze.append([0] + list(map(int,input().split())) + [0] )
maze.append([0]*(W+2))

res = 0
visited = [ [False]*(W+2) for _ in range(H+2) ]

def bfs(r,c):
  global res

  q = deque([(r,c)])
  while q:
    r,c = q.popleft()
    visited[r][c] = True

    moves_even = [[0, -1], [0, 1], [1, -1], [1, 0], [-1, 0], [-1, -1]]
    moves_odd = [[0, -1], [0, 1], [1, 1], [1, 0], [-1, 0], [-1, 1]]

    moves = moves_even if r%2==0 else moves_odd
    for x,y in moves:
      nx,ny = r+x,c+y
      if 0 <= nx < H+2 and 0 <= ny < W+2:
        if maze[nx][ny] == 1:
          res += 1
        else:
          if visited[nx][ny]: continue
          if (nx,ny) in q: continue
          q.append((nx,ny))

    # print(q)

bfs(0,0)
print(res)
for v in visited:
  print(v)