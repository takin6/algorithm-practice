from collections import deque

ans = []
while True:
  w,h = map(int,input().split())
  if w==h==0: 
    # for a in ans:
    #   print(a)
    exit()

  maze = []
  for k in range(h):
    # [(lower, right)]
    row = [ [0,0] for _ in range(w) ]
    
    for i in range(2):
      if i==0:
        # check for right boundary
        v = list(map(int,input().split()))
        for j in range(w-1):
          if v[j] == 1:
            row[j][1] = 1
      else:
        # check for lower boundary
        if k == h-1: continue
        v = list(map(int,input().split()))
        for j in range(w):
          if v[j] == 1:
            row[j][0] = 1

    maze.append(row)

  dist = [ [-1]*w for _ in range(h) ]
  dist[0][0] = 1
  q = deque([(0,0)])

  while q:
    r,c = q.popleft()

    directions = []

    # lower
    if maze[r][c][0] == 0:
      directions.append((1,0))

    # right
    if maze[r][c][1] == 0:
      directions.append((0,1))

    # upper
    if r-1>=0 and maze[r-1][c][0] == 0:
      directions.append((-1,0))

    # left
    if c-1>=0 and maze[r][c-1][1] == 0:
      directions.append((0,-1))


    for x,y in directions:
      nr,nc = r+x,c+y
      if 0 <= nr < h and 0 <= nc < w:
        if dist[nr][nc] != -1: continue
        if (nr,nc) in q: continue
        dist[nr][nc] = dist[r][c] + 1
        if nr == h-1 and nc == w-1:
          break
        else:
          q.append((nr,nc))

  if dist[h-1][w-1] == -1:
    ans.append(0)
    print(0)
  else:
    ans.append(dist[h-1][w-1])
    print(dist[h-1][w-1])


for a in ans:
  print(a)

# # import pprint
# for m in maze:
#   print(m)
# # print(maze)
# # [
# # [[0, 1], [1, 0]], 
# # [[1, 0], [0, 0]], 
# # [[0, 1], [0, 0]]
# # ]
# print("=======================")
# for di in dist:
#   print(di)


# [[0, 1], [0, 0], [0, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# [[0, 1], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
# [[0, 0], [0, 0], [0, 1], [1, 0], [1, 0], [0, 1], [1, 0], [1, 1], [0, 0], [1, 0], [1, 0], [0, 0]]
# [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]]
# [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1], [0, 0], [0, 0], [0, 0]]

# [1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# [2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# [3, 4, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1]
# [4, 5, 6, 7, 8, 9, -1, -1, -1, -1, -1, -1]
# [5, 6, 7, 8, 9, 10, 11, 12, 13, -1, -1, -1]