H,W,K,V = map(int,input().split())
matrix = []
for _ in range(H):
  matrix.append(list(map(int,input().split())))

if H==1 and W==1:
  if matrix[0][0] + K <= V:
    print(1)
  else:
    print(0)
  exit()

cs = [ [0]*(W+1) for _ in range(H+1) ]
for i in range(1, H+1):
  for j in range(1, W+1):
    cs[i][j] = matrix[i-1][j-1]+cs[i-1][j]+cs[i][j-1]-cs[i-1][j-1]

res = -10**15
for x1 in range(0,H+1):
  for y1 in range(0,W+1):

    for x2 in range(x1+1,H+1):
      for y2 in range(y1+1, W+1):
        masu = (x2-x1) * (y2-y1)
        area = cs[x2][y2] - cs[x2][y1] - cs[x1][y2] + cs[x1][y1]
        if area + (masu * K) <= V:
          res = max(res, masu)

print(max(res, 0))

# import sys
# input = sys.stdin.readline
 
# H, W, K, V = map(int, input().split())
# A = [[int(i) for i in input().split()] for _ in range(H)]
 
# s = [[0] * (W + 1) for _ in range(H + 1)]
# for y in range(H) :
#     for x in range(W) :
#         s[y+1][x+1] = A[y][x]
        
# for y in range(1, H + 1) :
#     for x in range(1, W + 1) :
#         s[y][x] += s[y-1][x] + s[y][x-1] - s[y-1][x-1]

# M = 0
# for ya in range(H + 1) :
#     for xa in range(W + 1) :
#         for yb in range(ya + 1, H + 1) :
#             for xb in range(xa + 1, W + 1) :
#                 print((ya,xa), (yb,xb))
#                 S = abs((xb - xa) * (yb - ya))
#                 import pdb; pdb.set_trace()
#                 if S <= M :
#                     continue
#                 if S * K + s[yb][xb] - s[ya][xb] - s[yb][xa] + s[ya][xa] <= V :
#                     M = S
                    
# print(M)


# print(cs)
# print(matrix)

