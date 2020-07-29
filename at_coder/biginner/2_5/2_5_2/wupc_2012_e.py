# for _ in range(M):
#   f,t,c = map(int, input().split())
#   for i in range(4):
#     if f != N-1:
#       four[4*f+i].append((c,4*t+(c+i)%4))
#     if t != N-1:
#       four[4*t+i].append((c,4*f+(c+i)%4))

#   for i in range(7):
#     if f!=N-1:
#       seven[7*f+i].append((c,7*t+(c+i)%7))
#     if t!=N-1:
#       seven[7*t+i].append((c,7*f+(c+i)%7))

# print(four)
# print(seven)

import heapq
INF = 10**100
def dijkstra(graph):
  R,C = len(graph), len(graph[0])
  visited = [False] * (R*C)
  dist = [INF] * (R*C)
  dist[0] = 0

  pq = [(0,0)]
  while pq:
    c,n = heapq.heappop(pq)
    visited[n] = True
    for nei,nc in graph[n]:
      if visited[nei]: continue
      if c+nc < dist[nei]:
        dist[nei] = c+nc
        heapq.heappush(pq, (c+nc, nei))

  return dist

N,M = map(int, input().split())
# four = [ [] for _ in range(4*N) for _ in range(N) ]
# seven = [ [] for _ in range(7*N) for _ in range(N) ]
four = [ [] for _ in range(4*N) ]
seven = [ [] for _ in range(7*N) ]

for _ in range(M):
  f,t,c = map(int, input().split())

  for i in range(4):
    if f != N-1:
      four[f*4+i].append([t*4+(c+i)%4, c])

    if t != N-1:
      four[t*4+i].append([f*4+(c+i)%4, c])

  for i in range(7):
    if f != N-1:
      seven[f*7+i].append([t*7+(c+i)%7, c])

    if t != N-1:
      seven[t*7+i].append([f*7+(c+i)%7, c])

cost_four = dijkstra(four)[(N-1)*4]
cost_seven = dijkstra(seven)[(N-1)*7]
print(min(cost_four, cost_seven))

# problem 
# https://atcoder.jp/contests/wupc2012-closed/tasks/wupc2012_5
#これを参考にもう一回実装する
# https://atcoder.jp/contests/wupc2012-closed/submissions/10705845

# 解説
# https://www.slideshare.net/hama_du/wupc2012
# http://tutuz.hateblo.jp/entry/2019/01/26/140539


# [[[8, 1]], [[9, 1]], [[10, 1]], [[11, 1]], [[12, 1]], [[13, 1]], [[7, 1]], [[1, 1], [15, 1]], [[2, 1], [16, 1]], [[3, 1], [17, 1]], [[4, 1], [18, 1]], [[5, 1], [19, 1]], [[6, 1], [20, 1]], [[0, 1], [14, 1]], [[8, 1], [22, 1]], [[9, 1], [23, 1]], [[10, 1], [24, 1]], [[11, 1], [25, 1]], [[12, 1], [26, 1]], [[13, 1], [27, 1]], [[7, 1], [21, 1]], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


# 4 3
# 0 1 1
# 1 2 1
# 2 3 1
# 