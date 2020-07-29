from collections import deque
H,W,K = map(int,input().split())
x1,y1,x2,y2 = map(int,input().split())

maze = []
maze.append(["@"]*(W+2))
for _ in range(H):
  row = list(input())
  maze.append(["@"]+row+["@"])
maze.append(["@"]*(W+2))

q = deque([(x1,y1)])
depth = 0
while q:
  for i,j in q:
    maze[i][j] = "@"

  new_q = set()
  l = len(q)
  for _ in range(l):
    x,y = q.pop()
    if (x,y) == (x2,y2):
      print(depth)
      exit()

    # Up
    for i in range(1, K+1):
      if maze[x-i][y] == "@": break
      new_q.add((x-i, y))

    # Down
    for i in range(1, K+1):
      if maze[x+i][y] == "@": break
      new_q.add((x+i, y))

    # Left
    for i in range(1, K+1):
      if maze[x][y-i] == "@": break
      new_q.add((x, y-i))

    # Right
    for i in range(1, K+1):
      if maze[x][y+i] == "@": break
      new_q.add((x, y+i))

  q = deque(list(new_q))
  depth += 1

print(-1)