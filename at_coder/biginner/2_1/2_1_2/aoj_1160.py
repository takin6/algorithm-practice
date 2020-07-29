# w,h = list(map(int, input().split()))
# C = []

# for _ in range(h):
#   C.append(list(map(int, input().split())))

# visited = []
# def dfs(i,j):
#   if i < 0 or i >= h or j < 0 or j >= w: return
#   if (i,j) in visited or C[i][j] == 0: return
#   # if C[i][j] == 0: return
#   visited.append((i,j))

#   dfs(i-1,j) or dfs(i+1,j) or dfs(i,j-1) or dfs(i,j+1) or dfs(i+1,j-1) or dfs(i-1,j+1) or dfs(i-1,j-1) or dfs(i+1,j+1)

import sys
sys.setrecursionlimit(10**7)

while True:
  w,h = list(map(int, input().split()))
  if w == 0 and h == 0:
    break
  C = []

  for _ in range(h):
    C.append(list(map(int, input().split())))

  visited = []

  def dfs(i,j):
    for x in range(-1,2):
      for y in range(-1,2):
        if i+x < 0 or i+x >= h or j+y < 0 or j+y >= w:
          continue
        else:
          if (i+x,j+y) in visited: continue
          if C[i+x][j+y] == 0: continue
          visited.append((i,j))
          dfs(i+x,j+y)

  cnt = 0
  for i in range(h):
    for j in range(w):
      if (i,j) not in visited and C[i][j] == 1:
        cnt += 1
        dfs(i,j)

  print(cnt)