import math

from collections import defaultdict

# N, x, y = list(map(int, input().split()))
# INF = math.inf
# adj_mtx = [ [INF] * (N+1) for _ in range(N+1) ]

# for i in range(1, N+1):
#   if i != N:
#     adj_mtx[i][i] = 0
#     adj_mtx[i][i+1] = 1
#     adj_mtx[i+1][i] = 1
# adj_mtx[x][y] = 1
# adj_mtx[y][x] = 1

# dic = defaultdict(int)

# # using warshall floyd algorithm : takes n^3
# for k in range(1, N+1):
#   for i in range(1, N+1):
#     for j in range(1, N+1):
#       tmp = min(adj_mtx[i][j], adj_mtx[i][k] + adj_mtx[k][j])
#       dic[tmp] = dic[tmp] + 1
#       adj_mtx[i][j] = tmp

# for v in range(1, N+1): print(dic[v])


N, X, Y = list(map(int, input().split()))
result = [0] * N


for i in range(1, N):
  for j in range(i+1, N+1):
    step = min( j-i, abs(i-X)+1+abs(j-Y), abs(i-Y)+1+abs(j-X))
    result[step] += 1

for e in result[1:]: print(e)