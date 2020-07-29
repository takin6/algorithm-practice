# import sys
# sys.setrecursionlimit(10**6)
# H,W = map(int,input().split())
# grid = []
# for _ in range(H):
#   grid.append(list(input()))

# def dfs(i,j,direction):
#   if i<0 or j<0 or i>=H or j>=W:
#     return 0
#   if grid[i][j] == "#":
#     return 0

#   if direction == "L":
#     return 1 + dfs(i,j-1,direction)
#   elif direction == "R":
#     return 1 + dfs(i,j+1,direction)
#   elif direction == "U":
#     return 1 + dfs(i+1,j,direction)
#   else:
#     return 1 + dfs(i-1,j,direction)

# res = 0
# for i in range(H):
#   for j in range(W):
#     if grid[i][j] != "#":
#       step = 1
#       for d in ["L","R","U","D"]:
#         ni,nj = i,j
#         if d=="L": nj = j-1
#         if d=="R": nj = j+1
#         if d=="U": ni = i+1
#         if d=="D": ni = i-1
#         step += dfs(ni,nj,d)
#       res = max(res, step)
#       if res == H+W-1:
#         print(res)
#         exit()

# print(res)

import sys
sys.setrecursionlimit(10**6)
H,W = map(int,input().split())
grid = []
for _ in range(H):
  grid.append(list(input()))

# L[i][j] = i行目j列目に明かりを置いたとき、そこから左に照らされるマスの個数
L = [ [0]*W for _ in range(H) ]
R = [ [0]*W for _ in range(H) ]
U = [ [0]*W for _ in range(H) ]
D = [ [0]*W for _ in range(H) ]

for i in range(H):
  for j in range(W):
    if j-1 >= 0:
      L[i][j] = L[i][j-1]
    if i-1 >= 0:
      D[i][j] = D[i-1][j]

    if grid[i][j] == ".":
      L[i][j] += 1
      D[i][j] += 1
    else:
      L[i][j] = 0
      D[i][j] = 0

for i in range(H-1,-1,-1):
  for j in range(W-1,-1,-1):
    if j+1 < W:
      R[i][j] = R[i][j+1] 
    if i+1 < H:
      U[i][j] = U[i+1][j]
    if grid[i][j] == ".":
      R[i][j] += 1
      U[i][j] += 1
    else:
      R[i][j] = 0
      U[i][j] = 0

res = 0
for i in range(H):
  for j in range(W):
    if grid[i][j] == ".":
      res = max(res, L[i][j]+R[i][j]+U[i][j]+D[i][j]-3)

print(res)