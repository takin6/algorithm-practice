# N = cities
# M = # of routes
# S = silver coin
# G = 10**100

# ith train
# Ui <=> Vi
# expense: Ai silver coin, time: Bi minutes 

# Q. minimum time to go from city1 to city t(2...N)

# - cannot pay by G
# - each city has exchange station 
# - ith exchange station can exchange 1 gold coin with Ci silver coins
# - takes Di minues / 1 gold coin

# N M S
# U1,V1,A1,B1
# ... 
# Un,Vn,An,Bn
# C1, D1
# ...
# Cn, Dn


# class Edge:
#   def __init__(self, to, a, b):
#     self.to = to
#     self.a = a
#     self.b = b

# MAX_V = 50
# MAX_S = MAX_V*50+5

# G = []
# N, M, S = list(map(int, input().split()))

# dp = [ [0] * (MAX_S+5) for _ in range(MAX_V)]
# for i in range(M):
#   u,v,a,b = 

import heapq
N,M,S = map(int,input().split())
MAX_COST = 2500
S = min(S, MAX_COST)

G = [ [] for _ in range(N) ]
for i in range(M):
  u,v,s,t = map(int,input().split())
  u, v = u-1, v-1
  G[u].append([v, s, t])
  G[v].append([u, s, t])

change_rate, change_cost = [], []
for i in range(N):
  rate, cost = map(int,input().split())
  change_rate.append(rate)
  change_cost.append(cost)

# dp[i][silver] = 頂点iにいて、銀貨をsilver枚持つときの最小時間
dp = [ [float('inf')]*(MAX_COST+1) for _ in range(N) ]
dp[0][S] = 0

# time,node,silver
pq = [(0,0,S)]
while pq:
  time,node,silver = heapq.heappop(pq)

  # going through exchange station
  next_silver = min(silver + change_rate[node], MAX_COST)
  next_time = time + change_cost[node]
  if next_time < dp[node][next_silver]:
    dp[node][next_silver] = next_time
    heapq.heappush(pq, (next_time, node, next_silver))

  for nei, ns, nt in G[node]:
    remain_silver = min(silver - ns, MAX_COST)
    if remain_silver < 0: continue

    next_time = time + nt
    if dp[nei][remain_silver] > next_time:
      dp[nei][remain_silver] = next_time
      heapq.heappush(pq, (next_time, nei, remain_silver))

for d in dp[1:]:
  print(min(d))


# https://at274.hatenablog.com/entry/2020/04/28/202045