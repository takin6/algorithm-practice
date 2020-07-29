from itertools import permutations
import math
N = int(input())
C = []
for _ in range(N):
  C.append(list(map(int,input().split())))

res = 0
cnt = 0
for pair in list(permutations(range(N), N)):
  for i in range(N):
    if i+1 == N: continue
    x,y = pair[i], pair[i+1]
    x_y = math.sqrt( (C[x][0]-C[y][0])**2 + (C[x][1]-C[y][1])**2 )
    res += x_y
  cnt += 1

print(res / cnt)

