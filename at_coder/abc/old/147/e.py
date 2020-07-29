# # (r,b) => (r,b) or (b,r)
# # (b,r) => (r,b) or (b,r)
# from collections import deque
# R,B = 1,0
# INF = 10**15
# H,W = map(int,input().split())
# A = [ [None]*W for _ in range(H) ]
# B = [ [None]*W for _ in range(H) ]
# for h in range(H):
#   for i,a in enumerate(list(map(int,input().split()))):
#     A[h][i] = a

# for h in range(H):
#   for i,b in enumerate(list(map(int,input().split()))):
#     B[h][i] = b

# # (r,c,red,blue)
# q = deque([(0,0,A[0][0],B[0][0]), (0,0,B[0][0],A[0][0])])
# move = [(1,0), (0,1)]
# res = INF
# while q:
#   r,c,red,blue = q.popleft()
#   if r==H-1 and c==W-1:
#     res = min(res, abs(red-blue))
#     continue

#   for y,x in move:
#     if r+y >= H or c+x >= W: continue
#     #(A,B) = (red,blue)
#     nr,nc = r+y, c+x
#     q.append((nr,nc,red+A[nr][nc],blue+B[nr][nc]))
#     q.append((nr,nc,red+B[nr][nc],blue+A[nr][nc]))

# print(res)


# H,W = map(int,input().split())
# A = [ [None]*W for _ in range(H) ]
# B = [ [None]*W for _ in range(H) ]
# for h in range(H):
#   for i,a in enumerate(list(map(int,input().split()))):
#     A[h][i] = a

# for h in range(H):
#   for i,b in enumerate(list(map(int,input().split()))):
#     B[h][i] = b

# dp = [ [ [False]*(81*(H+W)) for _ in range(W+1) ] for _ in range(H+1) ]
# dp[0][0][abs(A[0][0]-B[0][0])] = True

# for h in range(H):
#   for w in range(W):
#     for k in range(80*(H+W)):
#       if dp[h][w][k]:
#         if h+1 < H:
#           # (a,b) = (red,blue)
#           dp[h+1][w][abs(k-(abs(A[h+1][w]-B[h+1][w])))] = True
#           dp[h+1][w][abs(k+(abs(A[h+1][w]-B[h+1][w])))] = True

#         if w+1 < W:
#           # (a,b) = (red,blue)
#           dp[h][w+1][abs(k-(abs(A[h][w+1]-B[h][w+1])))] = True
#           dp[h][w+1][abs(k+(abs(A[h][w+1]-B[h][w+1])))] = True

# for i in range(81*H*W+1):
#   if dp[H-1][W-1][i]: 
#     print(i)
#     exit()
# print(dp[-1])


## bitset

import sys
input = sys.stdin.readline
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [list(map(int, input().split())) for _ in range(h)]
ab = [[0] * w for _ in range(h)]
for i in range(h):
  for j in range(w):
    ab[i][j] = abs(a[i][j] - b[i][j])
 
m = 80
dp = [[0] * w for _ in range(h)]
dp[0][0] = (1 << (m + ab[0][0])) | (1 << (m - ab[0][0]))
for i in range(h):
  for j in range(w):
    for dx, dy in [(1, 0), (0, 1)]:
      nx, ny = i + dx, j + dy
      if 0 <= nx < h and 0 <= ny < w:
        dp[nx][ny] = dp[nx][ny] | (dp[i][j] << ab[nx][ny])
        dp[nx][ny] = dp[nx][ny] | (dp[i][j] >> ab[nx][ny])

#print(dp[-1][-1])
for i in range(m+1):
  if (dp[h-1][w-1] >> i) & 1:
    ans = m - i
 
print(ans)


# https://matsu7874.hatenablog.com/entry/2019/12/09/004624