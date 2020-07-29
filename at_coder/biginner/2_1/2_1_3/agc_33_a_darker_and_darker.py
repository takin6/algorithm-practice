# import sys
# from collections import deque
# readline = sys.stdin.readline

# H,W = list(map(int, input().split()))
# matrix = [ list(readline()) for _ in range(H) ]
# black = deque([])
# seen = [ [False]*W for _ in range(H)]
# white = 0
# for ri,i in enumerate(matrix):
#   for ci,j in enumerate(matrix[i]):
#     if matrix[i][j] == "#":
#       black.append((i,j))


# for i in range(H):
#   row = list(readline().rstrip())
#   matrix.append(row)

#   for j in range(W):
#     if row[j] == "#":
#       black.append((i,j))
#     else:
#       white += 1

import sys
from collections import deque
readline = sys.stdin.readline

H,W = list(map(int, input().split()))
matrix = [ list(readline()) for _ in range(H) ]
black = deque([])
seen = [ [False]*W for _ in range(H)]
for ri,m in enumerate(matrix):
  for ci,j in enumerate(matrix[ri]):
    if j == "#":
      black.append((ri,ci))
      seen[ri][ci] = True

cnt = 0
while black:
  cnt += 1

  new_black = deque([])
  for i in range(len(black)):
    r,c = black[i]
    seen[r][c] = True

    for y,x in [(1,0),(-1,0),(0,1),(0,-1)]:
      nr,nc = r+y,c+x
      if nr<0 or nc<0 or nr>=H or nc>=W: continue
      if seen[nr][nc] or seen[nr][nc] == "#" or (nr,nc) in new_black: continue
      matrix[nr][nc] = "#"
      seen[r][c] = True
      new_black.append((nr,nc))

  black = new_black

print(cnt-1)

# cnt = 0
# while black:
#   cnt += 1

#   new_black = deque([])
#   for i in range(len(black)):
#     r,c = black.popleft()
#     seen[r][c] = True

#     for y,x in [(1,0),(-1,0),(0,1),(0,-1)]:
#       nr,nc = r+y,c+x
#       if nr<0 or nc<0 or nr>=H or nc>=W: continue
#       if seen[nr][nc] or seen[nr][nc] == "#" or (nr,nc) in new_black: continue
#       matrix[nr][nc] = "#"
#       seen[r][c] = True
#       new_black.append((nr,nc))

#   black = new_black

# print(cnt-1)