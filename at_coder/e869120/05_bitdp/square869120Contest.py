# from collections import Counter
# N,M = map(int,input().split())
# # N vertex, M nodes
# dist = [ [float('inf')]*N for _ in range(N)]
# times = [ [float('inf')]*N for _ in range(N)]
# for _ in range(M):
#   s,t,d,time = map(int,input().split())
#   s -= 1
#   t -= 1
#   dist[s][t] = d
#   dist[t][s] = d
#   times[s][t] = time
#   times[t][s] = time

# ans = Counter()
# dp = [ [-1]*N for _ in range(1<<N) ]
# path = [ [0]*N for _ in range(1<<N) ]
# VISITED_ALL = (1<<N) - 1

# def tsp(mask, pos, time):
#   # check memoization
#   if dp[mask][pos] != -1: 
#     return dp[mask][pos]

#   if mask == VISITED_ALL and pos == 0:
#     dp[mask][pos] = 0
#     path[mask][pos] = 1
#     return 0

#   res = float('inf')
#   for city in range(N):
#     # not visited
#     if (mask&(1<<city)) == 0:
#       x = dist[pos][city] + tsp(mask|(1<<city), city, time+dist[pos][city])
#       if x > times[pos][city]: continue
#       if x < res:
#         res = x
#         path[mask][pos] = path[mask|(1<<city)][city]
#       elif x == res:
#         path[mask][pos] += path[mask|(1<<city)][city]

#   dp[mask][pos] = res
#   return res 

# res = tsp(0,0,0)
# if res == float('inf'):
#   print("IMPOSSIBLE")
# else:
#   print(path)
#   print(res, path[0][0])


# dp[S][v] = 部分集合Sを巡回する経路のうち、最短のものの距離と経路数のペア

# N,M = map(int,input().split())
# INF = float('inf')
# dist = [ [INF]*N for _ in range(N) ]
# times = [[INF]*N for _ in range(N)]
# for _ in range(M):
#   s,t,d,time = map(int,input().split())
#   s -= 1
#   t -= 1
#   dist[s][t] = d
#   times[t][s] = time

# dp = [[-1]*N for _ in range(1<<N)]
# path = [[0]*N for _ in range(1<<N)]
# VISITED_ALL = (1<<N)-1
# def tsp(mask, pos, d):
#   if dp[mask][pos] > 0: return dp[mask][pos]

#   if mask == VISITED_ALL:
#     dp[mask][pos] = 0
#     path[mask][pos] = 1
#     return 0

#   res = INF
#   for city in range(N):
#     if (1<<city)&mask == 1: continue
#     x = dist[pos][city] + tsp(mask|1<<city, city, d+dist[pos][city])
#     if x > times[pos][city]: continue
#     if x < res:
#       res = x
#       path[mask][pos] = path[mask|1<<city][city]
#     else:
#       path[mask][pos] += path[mask|1<<city][city]

#   dp[mask][pos] = res
#   return dp[mask][pos]

# ans = tsp(1,0,0)
# for p in path:
#   print(p)

import sys
sys.setrecursionlimit(10 ** 7)
 
INF = float("inf")
n, m = map(int, input().split())
dist = [[INF] * n for _ in range(n)]
times = [[INF] * n for _ in range(n)]
for i in range(m):
  s, t, d, time = map(int, input().split())
  s -= 1
  t -= 1
  dist[s][t] = d
  dist[t][s] = d
  times[s][t] = time
  times[t][s] = time

# dp[mask][pos] = maskの状態で、posにたどり着くときの最短距離
dp = [[-1] * n for _ in range(1 << n)]
# path[mask][pos] = maskの状態でposにたどり着くときに、最短距離を実現できる回数
path = [[0] * n for _ in range(1 << n)]
VISITED_ALL = (1<<n)-1

def tsp(s, v):
  print(v, bin(s))
  if dp[s][v] > 0: return dp[s][v]

  # if s == VISITED_ALL and v == 0:
  if s == VISITED_ALL:
    print("visited_all", v, bin(s))
    dp[s][v] = 0
    path[s][v] = 1
    return 0

  ans = INF
  for u in range(n):
    if s & (1<<u): continue
    newAns = dist[v][u] + tsp(s|1<<u, u)
    if newAns > times[v][u]: continue
    if newAns < ans:
      ans = newAns
      path[s][v] = path[s|1<<u][u]
    elif newAns == ans:
      path[s][v] += path[s|1<<u][u] 

  dp[s][v] = ans
  return dp[s][v]

res = tsp(0,0)
if res == float("inf"):
  print("IMPOSSIBLE")
else:
  print(res, path[0][0])
