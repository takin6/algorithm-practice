from collections import deque
H,W = map(int,input().split())
maze = []
for _ in range(H):
  maze.append(list(input()))

res = 0
move = [(1,0),(0,1),(0,-1),(-1,0)]
for i in range(H):
  for j in range(W):
    if maze[i][j] == ".":
      visited = [[False]*W for _ in range(H) ]
      q = deque([(i,j)])
      depth = -1
      while q:
        depth += 1
        L = len(q)
        new = deque([])
        for _ in range(L):
          i,j = q.popleft()
          if visited[i][j]: continue
          visited[i][j] = True
          for y,x in move:
            if 0<=i+y<H and 0<=j+x<W and not visited[i+y][j+x]:
              if maze[i+y][j+x] == ".":
                new.append((i+y,j+x))
        q = new
      res = max(res, depth)

print(res)


