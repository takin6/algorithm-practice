# 1. use deque library
# 2. use readline
# 3. add visited[nr][nc] or (nr,nc,step+1) in q condition
# 4. use array as visited
# 5. mark visited while parsing the array

import sys
readline = sys.stdin.readline
from collections import deque
H,W = list(map(int, input().split()))
matrix = []
blocks = 0
for _ in range(H):
  # row = list(input())
  row = readline().rstrip()
  blocks += row.count("#")
  matrix.append(row)

q = deque([(0,0,0)])
min_step = -1
# visited = []
visited = [ [False]*W for _ in range(H) ]
visited[0][0] = True

while q:
  r,c,step = q.popleft()

  for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
    nr,nc = r+i,c+j
    if nr==H-1 and nc==W-1: 
      min_step = step+1
      q = []
      break

    if nr<0 or nc<0 or nr>=H or nc>=W: continue
    if visited[nr][nc] or (nr,nc,step+1) in q: continue
    # if (nr,nc) in visited: continue
    if matrix[nr][nc] == "#": continue
    visited[r][c] = True
    q.append((nr,nc,step+1))

if min_step == -1:
  print(-1)
else:
  print( H*W - blocks - min_step -1 )

