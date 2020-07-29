import sys
sys.setrecursionlimit(10**6)
from itertools import product
while True:
  w,h = map(int,input().split())
  if w == h == 0: exit()
  islands = []
  for _ in range(h):
    islands.append(list(map(int,input().split())))

  seen = [ [False]*w for _ in range(h) ]
  def dfs(row,col):
    seen[row][col] = True

    for x,y in product(range(-1,2), repeat=2):
      if x==0 and y==0: continue
      nrow, ncol = row+x, col+y
      if nrow>=h or nrow<0 or ncol>=w or ncol<0: continue
      if seen[nrow][ncol]: continue

      if islands[nrow][ncol] == 1:
        dfs(nrow, ncol)

  res = 0
  for i in range(h):
    for j in range(w):
      if islands[i][j] == 1 and not seen[i][j]:
        dfs(i,j)
        res += 1

  print(res)
